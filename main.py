import MODULES.ScanPort as ScanPort
import MODULES.pdfGeneral as pdfGen
import MODULES.searchsploitCli as searchsploit

network2scan = "127.0.0.1"
scan = ScanPort.Nmap(network2scan)
scandict = pdfGen.nmap_dictionarisation(scan)

with open('./AUDIT_TEMPLATE/OUTPUT.md', 'w') as outfile:
    outfile.write(pdfGen.generate_markdown(scan))

for scan in scandict:
    print(searchsploit.exploitdbSearch(scan['product'] + ' ' + scan['version'].split(' ')[0]))
