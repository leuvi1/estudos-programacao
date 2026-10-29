import time
import schedule

def executar_rotina_geral():
    print("\n[AGENDADOR] Iniciando a rotina automática de relatórios...")
    # Aqui dentro poderiamos chamar os scripts anteriores ou integrar as funções
    print("[AGENDADOR] 1. Consolidando dados de vendas...")
    print("[AGENDADOR] 2. Separando relatórios por filial...")
    print("[AGENDADOR] 3. Disparando e-mails em lote...")
    print("[AGENDADOR] 4. Rotina concluída com sucesso! Aguardando o próximo ciclo...")

# Exemplo de agendamento (Pode configurar para dias da semana ou horários específicos)
# schedule.every().monday.at("08:00").do(executar_rotina_geral)

# Para testes imediatos, podemos agendar para rodar a cada 10 segundos: 
schedule.every(10).seconds.do(executar_rotina_geral)  

print("Agendador ativado e rodando em segundo plano.")
print("Pressione Ctrl + C no terminal pra encerrar o agendador a qualquer momento. ")

# Loop contínuo que mantém o script escutando o tempo
while True:
    schedule.run_pending()
    time.sleep
