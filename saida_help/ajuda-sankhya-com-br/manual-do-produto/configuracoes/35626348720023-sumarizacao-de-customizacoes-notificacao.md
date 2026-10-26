---
id: "35626348720023"
titulo: "Sumarização de Customizações - notificação de tempo de execução em customizações"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35626348720023-Sumariza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es-notifica%C3%A7%C3%A3o-de-tempo-de-execu%C3%A7%C3%A3o-em-customiza%C3%A7%C3%B5es"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:43:20Z"
rotulos: ["Configuração", "Relatórios", "Monitoramento", "TELEMTLIMITE", "PTELEMTLIMITE", "br.com.sankhya.mge.sumarizacao.customizacao", "Desempenho", "Customização"]
---

# Sumarização de Customizações - notificação de tempo de execução em customizações

**Versão Mínima:** 4.35
**Caminho de Acesso:** Menu Principal > Configurações > Relatórios > Sumarização de Customizações

---

## Sumário

- [Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/35626348720023-Sumariza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es-notifica%C3%A7%C3%A3o-de-tempo-de-execu%C3%A7%C3%A3o-em-customiza%C3%A7%C3%B5es#h_01K7HWFMQRXBHX23PGNKRKJSGT)
  - [1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/35626348720023-Sumariza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es-notifica%C3%A7%C3%A3o-de-tempo-de-execu%C3%A7%C3%A3o-em-customiza%C3%A7%C3%B5es#h_01K7HWFMQTJRA2K7VVW0KEX1HD)
  - [2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/35626348720023-Sumariza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es-notifica%C3%A7%C3%A3o-de-tempo-de-execu%C3%A7%C3%A3o-em-customiza%C3%A7%C3%B5es#h_01K7HWHTC00SA1FS8BNV4NE59N)
  - [3. Diagrama de Fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/35626348720023-Sumariza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es-notifica%C3%A7%C3%A3o-de-tempo-de-execu%C3%A7%C3%A3o-em-customiza%C3%A7%C3%B5es#h_01K7HWFMRD2NRMD3A1NWZZRDT8)
  - [4. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/35626348720023-Sumariza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es-notifica%C3%A7%C3%A3o-de-tempo-de-execu%C3%A7%C3%A3o-em-customiza%C3%A7%C3%B5es#h_01K7HWG5G8AFX3412G40XEJ27N)
  - [5. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/35626348720023-Sumariza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es-notifica%C3%A7%C3%A3o-de-tempo-de-execu%C3%A7%C3%A3o-em-customiza%C3%A7%C3%B5es#h_01K7HWFMRW0X5EBA7X9JE59C4J)
  - [6. Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/35626348720023-Sumariza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es-notifica%C3%A7%C3%A3o-de-tempo-de-execu%C3%A7%C3%A3o-em-customiza%C3%A7%C3%B5es#h_01K7HWFMSKVP3HHBDQ3T5CB4KP)
  - [7. Casos de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/35626348720023-Sumariza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es-notifica%C3%A7%C3%A3o-de-tempo-de-execu%C3%A7%C3%A3o-em-customiza%C3%A7%C3%B5es#h_01K7HWJQYH0CMSWR8ZJ4TDPSK4)
- [FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/35626348720023-Sumariza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es-notifica%C3%A7%C3%A3o-de-tempo-de-execu%C3%A7%C3%A3o-em-customiza%C3%A7%C3%B5es#h_01K7HWJWJR4SG2FA44RW3N7XYE)

---

## Descrição e Usabilidade

---

### 1. Descrição da Funcionalidade

A funcionalidade **Notificação de Tempo de Execução em Customizações** visa monitorar a execução dos serviços consumidos pela tela, abrangendo tanto o **código nativo** quanto o **código customizado** do sistema.

Sempre que, durante um processo, algum objeto customizado apresentar um tempo de execução elevado em comparação ao tempo total da operação, o usuário será alertado.

O tempo apresentado é o **somatório do tempo gasto pelos serviços nativos e customizados**.

Por exemplo, em determinada execução, foi chamado um serviço que teve **duas personalizações**, com tempos de **3.001 ms** e **3.154 ms**, totalizando **6.155 ms** para as customizações. O tempo gasto pelo serviço nativo foi de **161 ms**, resultando em um **tempo total de execução de 6.316 ms**. Neste caso, a seguinte mensagem surge na tela:

"Algumas personalizações estão impactando o desempenho e prolongando a execução do processo. Clique aqui para ver os detalhes"

![Imagem 1: "Algumas personalizações estão impactando o desempenho e prolongando a execução do processo. Clique aqui para ver os…](https://ajuda.sankhya.com.br/hc/article_attachments/35626348708759)

Quando isso ocorre, um aviso é exibido na tela, permitindo ao usuário visualizar detalhes sobre o tempo gasto por cada customização, facilitando a identificação de gargalos e promovendo maior eficiência no uso do sistema.

![Imagem 2: Quando isso ocorre, um aviso é exibido na tela, permitindo ao usuário visualizar detalhes sobre o tempo gasto por cada…](https://ajuda.sankhya.com.br/hc/article_attachments/35626348709143)

Além do aviso em tempo real, a tela **“Sumarização de Customizações”** oferece uma visão detalhada das execuções, permitindo análise por usuário, tela e serviço, com informações sobre cada chamada, somatórios e descrições detalhadas das operações realizadas.

---

### 2. Pré-requisitos

- **Parâmetros essenciais**:
  - **TELEMTLIMITE**: define o tempo mínimo (em segundos) de chamadas que serão monitoradas.
  - **PTELEMTLIMITE:** define o percentual do tempo gasto em customizações a partir do qual os alertas serão gerados.
- **Configurações relacionadas**:
  - Customizações devidamente cadastradas no sistema.
  - Parâmetros ajustados conforme a necessidade do negócio.

---

### 3. Diagrama de fluxo

![Imagem 3: 3. Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/article_attachments/35626348709271)

---

### 4. Jornada de Uso

1. O usuário executa um processo no sistema, por exemplo, **alteração de uma nota**.
2. Durante a execução, o sistema **monitora os objetos personalizados**, como **eventos, callbacks e regras de negócio**, além do tempo total da operação.
3. Se o **tempo consumido pelas customizações** exceder os limites definidos nos parâmetros do sistema, um **aviso é exibido na tela**, destacando o impacto das personalizações no desempenho.
4. O sistema monitora o tempo total da operação e o tempo consumido por cada customização.
5. Se o tempo de customização exceder os limites definidos pelos parâmetros, um aviso é exibido na tela.
6. Então, você pode clicar em **“Clique aqui para ver os detalhes”** para acessar a tela de detalhamento.
7. Caso queira, o sistema ainda possui a tela **“Sumarização de Customizações”**, é possível visualizar as informações detalhadas sobre cada operação, incluindo tempos individuais e totais.
8. O usuário pode analisar os dados para identificar possíveis gargalos e tomar ações corretivas.

---

### 5. Pontos de Atenção

Os parâmetros **TELEMTLIMITE** e **PTELEMTLIMITE** devem ser configurados conforme a realidade do negócio, garantindo que os alertas de desempenho sejam relevantes e evitando notificações excessivas ou a falta de avisos importantes.

- **TELEMTLIMITE**: define o tempo mínimo (em segundos) de chamadas que serão monitoradas.
  - Valor padrão: 2 segundos
  - Limites permitidos: entre 2 e 5 segundos
- PTELEMTLIMITE: define o percentual do tempo gasto em customizações a partir do qual os alertas serão gerados.
  - Valor padrão: 30%
  - Limites permitidos: entre 1% e 49%

**Observação:** o parâmetro percentual só é avaliado se o tempo de execução ultrapassar o limite definido em **TELEMTLIMITE**.

O aviso de desempenho é exibido apenas quando as customizações ultrapassam os limites configurados. Customizações mal otimizadas podem impactar significativamente o desempenho do sistema, portanto é essencial ajustar esses parâmetros de forma realista.

---

### 6. Dicas de Usabilidade

- Utilize a tela **“Sumarização de Customizações”** para monitorar periodicamente o desempenho das customizações.
- Ajuste os parâmetros de tempo conforme a complexidade dos processos e a atuação esperada.
- Analise os detalhes das execuções para identificar e corrigir customizações que estejam consumindo tempo excessivo.

---

### 7. Casos de Uso

✅ **Exemplo Real:**
Durante a alteração de um usuário ou de uma nota, o sistema monitora o tempo total da operação e o tempo consumido pelas customizações.

Por exemplo, considerando os valores padrão dos parâmetros:

- **TELEMTLIMITE:** 2 segundos
- **PTELEMTLIMITE:** 30%

Se o tempo total de uma alteração no cabeçalho e nota for 3 segundos e o percentual de tempo consumido por customizações ultrapassar 30%, o sistema exibirá um aviso de desempenho.

O usuário pode então acessar os detalhes da execução, identificar a customização responsável pelo consumo elevado e acionar a equipe técnica para otimização, garantindo melhor desempenho nas operações futuras.

❌ **Erro Comum:**
Os parâmetros de tempo não estão configurados corretamente, resultando em ausência de avisos mesmo quando há lentidão perceptível nas operações.

---

## FAQ – Dúvidas Frequentes

1. **O que acontece se o tempo de customização ultrapassar o limite?**
   O sistema exibe um aviso na tela, permitindo ao usuário acessar detalhes sobre o tempo gasto por cada customização.
2. **Como posso ajustar os limites de tempo para os avisos?**
   Ajuste os parâmetros TELEMTLIMITE (tempo em segundos) e PTELEMTLIMITE (percentual) conforme a necessidade do seu negócio.
3. **Consigo visualizar o histórico de execuções e tempos?**
   Sim, utilize a tela “Sumarização de Customizações” para acessar dados detalhados por usuário, tela e serviço.
4. **O aviso impacta a execução do processo?**
   Não, o aviso é apenas informativo e não impede a conclusão da operação.
