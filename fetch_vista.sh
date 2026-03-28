#!/usr/bin/env bash
# Fetch all outstanding VistA documents (non-VistA packages excluded)
set -euo pipefail

PKGS=(
  ACKQ ACR AFJX AMT ANRV AR/WS ASCD ASU BMS CAPRI CCRA CDSP CHDS CISS CPRS CPT CRHD
  CRMS DGBT DGJ DI DRM+ DVBA EAS EC EDIS EFR EHM EN EPI EPSI ETS FFP FH FIM FMDC
  GEN GMPL GMRA GMRV GMTS HBPC HINQ IBD IFR IVM IVMB KDC KMPD KMPR KMPS KMPV LEDI
  LEX LHS MC MD MED MJCF MMRS MPIF NCR NPM NUMI NUPA NUR ONC OOPS PAIT PCMM PECS POC
  PPP PRC PRCN PREA PRED PREM PRPF PRS PSA PSJ PSN PSS PSU PSX PX PXRM QAC QAM QAO
  QAP RMPR ROEB ROEG ROES ROEV ROR RT RUM SAGG SAMH SD SPN SQLI SRA SSO/UC STS TBI
  TMP VALM VAP VAQ VDEF VES VHIC VIAB VODA VPFS VPR WII WV XM XOBE XOBV XOBW XQOR
  XT XU
)

LOG=/home/rafael/data/vista-docs/fetch_vista.log
VENV=/home/rafael/projects/vista-docs/.venv/bin/vista-docs

echo "Started: $(date)" | tee "$LOG"
echo "Packages: ${#PKGS[@]}" | tee -a "$LOG"

for pkg in "${PKGS[@]}"; do
  echo "" | tee -a "$LOG"
  echo "=== $pkg ===" | tee -a "$LOG"
  "$VENV" fetch --pkg "$pkg" 2>&1 | tee -a "$LOG" || true
done

echo "" | tee -a "$LOG"
echo "Finished: $(date)" | tee -a "$LOG"
