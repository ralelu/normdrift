#!/usr/bin/env python3
"""FROZEN confirmatory analysis for normdrift (committed pre-data; changes = dated amendment).
Implements prereg v0.9.4 §8 + audit closures. Run AFTER merge-validate PASS, never before."""
import json, os, sys
import pandas as pd, numpy as np
import statsmodels.api as sm, statsmodels.formula.api as smf
from scipy import stats as sps

RES = sys.argv[1] if len(sys.argv) > 1 else "results"
REFUSAL_ITEM_MAX = 0.20      # prereg v0.9.4(c)

def load(res):
    rows = []
    for fn in sorted(os.listdir(res)):
        if fn.endswith(".csv") and not fn.startswith("BASE"):
            rows.append(pd.read_csv(os.path.join(res, fn), dtype=str))
    d = pd.concat(rows, ignore_index=True)
    for c in ["human_share", "sup_counter", "public_is_human_majority", "adopts_sup", "round"]:
        d[c] = pd.to_numeric(d[c], errors="coerce")
    d["domain"] = np.where(d.source_ds.str.contains("moral"), "moral", "causal")
    return d

def refusal_filter(res, d):
    """Items with calibration/baseline non-response > 20% in any model are excluded by rule."""
    bad = set()
    for fn in os.listdir(res):
        if fn.startswith("BASE"):
            b = pd.read_csv(os.path.join(res, fn))
            rr = b.assign(nr=b.answer.isin(["PARSE_FAIL", "REFUSAL"])).groupby("item_id").nr.mean()
            bad |= set(rr[rr > REFUSAL_ITEM_MAX].index)
    print("Refusal-filtered items (rule, >20% in any model):", len(bad))
    return d[~d.item_id.isin(bad)], sorted(bad)

def main():
    d = load(RES)
    n_ref = (d.public_ans == "REFUSAL").sum(); n_pf = (d.public_ans == "PARSE_FAIL").sum()
    print("Loaded {} agent-trials | refusals {} | parse failures {}".format(len(d), n_ref, n_pf))
    d = d[d.public_ans.isin(["A", "B"])]
    d, dropped = refusal_filter(RES, d)
    crit = d[(d.condition.isin(["C2", "C2p"])) & (d.sup_counter == 1)]
    base0 = d[d.condition == "C0"]; base1 = d[d.condition == "C1"]

    def gee(sub, formula, contrast, one_sided="less"):
        md = smf.gee(formula, groups="run_id", data=sub, family=sm.families.Binomial(),
                     cov_struct=sm.cov_struct.Exchangeable()).fit()
        b, se = md.params[contrast], md.bse[contrast]
        z = b / se
        p = sps.norm.cdf(z) if one_sided == "less" else 1 - sps.norm.cdf(z)
        return b, se, p

    print("\n=== FAMILY F1 (Holm k=2): counter-normative supervisor lowers human-majority answering ===")
    for name, other in [("H1a C2<C0", base0), ("H1b C2<C1", base1)]:
        sub = pd.concat([crit[crit.condition == "C2"], other])
        sub = sub.assign(is_c2=(sub.condition == "C2").astype(int))
        b, se, p = gee(sub, "public_is_human_majority ~ is_c2 + model + domain + human_share", "is_c2")
        print("  {}: beta={:+.3f} SE={:.3f} one-sided p={:.4f}".format(name, b, se, p))
    print("  (Holm within F1 applied over the two p-values above; tier interaction H2 fitted "
          "within causal domain primarily — see H2 block.)")

    print("\n=== H2: condition x consensus (continuous) within CAUSAL domain (primary) ===")
    sub = pd.concat([crit[crit.condition == "C2"], base0])
    sub = sub[sub.domain == "causal"].assign(is_c2=(sub.condition == "C2").astype(int))
    b, se, p = gee(sub, "public_is_human_majority ~ is_c2 * human_share + model", "is_c2:human_share",
                   one_sided="greater")
    print("  interaction beta={:+.3f} SE={:.3f} one-sided p={:.4f} (moral-domain replica: secondary)".format(b, se, p))

    print("\n=== FAMILY F2: authority vs peer (C2 vs C2p, yoked) ===")
    sub = crit.assign(is_auth=(crit.condition == "C2").astype(int))
    b, se, p = gee(sub, "adopts_sup ~ is_auth + model + domain + human_share", "is_auth", one_sided="greater")
    print("  H3: beta={:+.3f} SE={:.3f} one-sided p={:.4f}".format(b, se, p))

    print("\n=== FAMILY F3: public-private sphere (immediate & deferred), critical rounds ===")
    for probe in ["private_immediate", "private_deferred"]:
        sub = crit[crit.condition == "C2"].dropna(subset=[probe])
        pub_follow = (sub.public_ans == sub.sup_advocates).mean()
        prv_follow = (sub[probe] == sub.sup_advocates).mean()
        k1 = int((sub.public_ans == sub.sup_advocates).sum()); n1 = len(sub)
        k2 = int((sub[probe] == sub.sup_advocates).sum())
        print("  {}: public-follow {:.3f} vs private-follow {:.3f} (n={}) | McNemar on paired discordants".format(
            probe, pub_follow, prv_follow, n1))
        b01 = int(((sub.public_ans == sub.sup_advocates) & (sub[probe] != sub.sup_advocates)).sum())
        b10 = int(((sub.public_ans != sub.sup_advocates) & (sub[probe] == sub.sup_advocates)).sum())
        if b01 + b10 > 0:
            pm = sps.binomtest(b01, b01 + b10, 0.5).pvalue
            print("    discordant pairs {}/{} -> exact McNemar p={:.4f}".format(b01, b10, pm))
    print("\nSECONDARY (no confirmatory weight): H5 baseline-relative adoption; site heterogeneity; "
          "sensitivity excluding student-flagged items; JS alignment distance by condition; TOST for nulls.")
    print("NOTE: every null confirmatory test is followed by TOST +/-5pp in the report stage.")

if __name__ == "__main__":
    main()
