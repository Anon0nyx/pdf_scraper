pdftotext -layout ../apt_list.pdf
head -n 12693 apt_list.txt > apt_list.temp
tail -n 12340 apt_list.temp > apt_list.txt
rm apt_list.temp

# Organize sections better
perl -i -pe's/,/[comma]/g' apt_list.txt
perl -i -pe's/Names/#Names#/' apt_list.txt
perl -i -pe's/Country/#Country#/' apt_list.txt
perl -i -pe's/Sponsor/#Sponsor#/' apt_list.txt
perl -i -pe's/Motivation/#Motivation#/' apt_list.txt
perl -i -pe's/Description/#Description#/' apt_list.txt
perl -i -pe's/Observed/#Observed#/' apt_list.txt
perl -i -pe's/Tools used/#Tools used#/' apt_list.txt
perl -i -pe's/Tool used/#Tools used#/' apt_list.txt
perl -i -pe's/^Information/#Information#/' apt_list.txt
perl -i -pe's/^Operations/#Operations#/' apt_list.txt
perl -i -pe's/^Counter/#Counter#/' apt_list.txt
perl -i -pe's/^MITRE ATT&CK/#MITRE ATT&CK#/' apt_list.txt

perl -i -pe'/^[[:space:]]*$/d' apt_list.txt
