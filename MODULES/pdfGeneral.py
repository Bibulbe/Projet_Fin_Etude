# Importez les bibliothèques nécessaires
import io
from markdown import markdown
from weasyprint import HTML

def md2pdf():
    # Définissez le contenu Markdown
    with open('../AUDIT_TEMPLATE/AUDIT_TEMPLATE.md', 'r') as txt:
        markdown_content = txt.read()

    # Convertissez le contenu Markdown en HTML
    html_content = markdown(markdown_content)

    # Créez un fichier PDF en mémoire
    pdf_buffer = io.BytesIO()
    HTML(string=html_content).write_pdf(pdf_buffer)

    # Récupérez les données du PDF en mémoire
    pdf_data = pdf_buffer.getvalue()

    # Ouvrez un fichier en écriture
    with open('file.pdf', 'wb') as f:
        # Écrivez les données du PDF dans le fichier
        f.write(pdf_data)


def list2graphical(varlist):
    returnlist = ''
    for ligne in varlist:
        returnlist += ('- ' + ligne + ' \n')
    return returnlist


def dict2bckreturn(varlist):
    returnvalue = ''
    for ligne in varlist:
        returnvalue += (
            '{port}/{protocol}:{product}-{version}<br>'.format(port=ligne['port'], protocol=ligne['protocol'],
                                                               product=ligne['product'], version=ligne['version']))
    return returnvalue


def nmap_dictionarisation(nm):
    services = []
    for host in nm.all_hosts():
        for protocol in nm[host].all_protocols():
            lport = nm[host][protocol].keys()
            for port in lport:
                product = nm[host][protocol][port]['product']
                version = nm[host][protocol][port]['version']
                state = nm[host][protocol][port]['state']
                services.append({'port': port, 'protocol': protocol, 'product': product, 'version': version})
    return services


def nmap2table(nm):
    returnlist = ''
    services = []
    for host in nm.all_hosts():
        for protocol in nm[host].all_protocols():
            lport = nm[host][protocol].keys()
            for port in lport:
                product = nm[host][protocol][port]['product']
                version = nm[host][protocol][port]['version']
                state = nm[host][protocol][port]['state']
                services.append({'port': port, 'protocol': protocol, 'product': product, 'version': version})
        returnlist += (
            '| {ip}| {nom}| {services}|\n'.format(ip=host, nom=nm[host].hostname(), services=dict2bckreturn(services)))
    return returnlist


def generate_markdown(nmap):
    with open('./AUDIT_TEMPLATE/AUDIT_TEMPLATE.md', 'r') as f:
        outvalue = (f.read().format(networklist=list2graphical(nmap.all_hosts()), listeIPtable=nmap2table(nmap)))
        return outvalue


if __name__ == "__main__":
    import nmap
    import ScanPort

    network2scan = "127.0.0.1/31"
    scan = ScanPort.Nmap(network2scan)

    print(generate_markdown(scan))
