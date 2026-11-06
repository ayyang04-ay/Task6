# Upload target for mmc5.xlsx

Drop the original `mmc5.xlsx` (Supplementary Table 10, Mucosal Immunology
10.1016/j.mucimm.2024.12.001, PMC11982439) in this directory, unedited.

`mmc5.xlsx` is ~133 MB. GitHub rejects any single file over 100 MB on a normal
push, so it needs Git LFS:

    git lfs install
    git lfs track "data_room/*.xlsx"
    git add .gitattributes data_room/mmc5.xlsx
    git commit -m "Mount mmc5 (original, unedited)"
    git push -u origin claude/ax1177-il33-mechanistic

Without LFS the push fails with "file is 133.00 MB; this exceeds GitHub's file
size limit of 100.00 MB".

Do not strip workbook metadata before uploading. The metadata strip is a build
step applied to a copy; the original stays as delivered so provenance can be
re-checked.
