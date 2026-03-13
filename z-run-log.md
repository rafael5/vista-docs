# 1. Survey the full expanded corpus
python3 scripts/corpus_survey.py --manifest scripts/guides-manifest.json > scripts/survey-report-v2.txt

# 2. Check the new packages specifically
python3 corpus_survey.py --manifest scripts/guides-manifest.json --pkg TIU,GMRC,SD,PSO,PSJ,LR,RA,SR,ECX > scripts/survey-report-new-pkgs.txt


python3 scripts/corpus_survey.py --manifest scripts/guides-manifest.json > scripts/survey-report-v2.txt
