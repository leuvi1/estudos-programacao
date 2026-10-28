import os
import smtplib
from email.message import EmailMessage

print("Iniciando a preparação do envio de e-mails...")

# Configurações do Servidor de E-mail (Exemplo corporativo / Gmail)
# Nota: Para contas reais, utilize uma Senha de Aplicativo (App Password) do seu provedor.
EMAIL_ORIGEM = "seu_email@dominio.com"
SENHA_EMAIL = "sua_senha_de_aplicativo"

destinatario = "gerente_filial@dominio.com"
assunto = "Relatório Automatizado de Vendas - Por Filial"
corpo_mensagem = """
Olá,

Segue em anexo o relatório automatizado de vendas atualizado correspondente à sua filial.
Qualquer dúvida, estamos à disposição.

Atenciosamente,
Sistema de Automação de Processos
"""

# Montagem da mensagem de e-mail
msg = EmailMessage()
msg['Subject'] = assunto
msg['From'] = EMAIL_ORIGEM
msg['To'] = destinatario
msg.set_content(corpo_mensagem)

# Caminho para anexar o relatório gerado no projeto anterior
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_anexo = os.path.join(diretorio_atual, "Ficheiros_Excel", "Relatorios_Filiais", "Relatorio_São_Paulo.xlsx")

# Verifica e adiciona o anexo de forma segura
if os.path.exists(caminho_anexo):
    with open (caminho_anexo, "rb") as arquivo:
        dados_arquivo = arquivo.read()
        nome_arquivo = os.path.basename(caminho_anexo)
    
    msg.add_attachment(dados_arquivo, maintype="application", subtype="xlsx", filename=nome_arquivo)
    print(f"Anexo '{nome_arquivo}' carregado com sucesso.")
else:
    print(f"Aviso: O arquivo para anexo não foi encontrado em: {caminho_anexo}")

print("Estrutura do e-mail configurada com sucesso. (Insira suas credenciais reais para efetuar o disparo no servidor SMTP)")
