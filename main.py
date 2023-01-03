import MODULES.ScanPort as ScanPort
import MODULES.pdfGeneral as pdfGen

network2scan = "127.0.0.1/31"
scan = ScanPort.Nmap(network2scan)

with open('./AUDIT_TEMPLATE/OUTPUT.md', 'w') as outfile:
    outfile.write(pdfGen.generate_markdown(scan))

print(pdfGen.nmap_dictionarisation(scan))
