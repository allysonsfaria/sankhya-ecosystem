---
id: "33685324137495"
titulo: "Gestão de Frotas - Integração com rastreadores"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33685324137495-Gest%C3%A3o-de-Frotas-Integra%C3%A7%C3%A3o-com-rastreadores"
trilha: "Sankhya Official Pack - SOP > Frotas"
atualizado_em: "2026-07-22T14:28:36Z"
rotulos: ["Configuração", "Integração", "br.com.sankhya.core.cad.veiculos", "br.com.sankhya.soplogistica.cad.configuracao.gestao", "Gestão de Frotas", "Logística", "Rastreadores"]
---

# Gestão de Frotas - Integração com rastreadores

### Integração com Rastreadores

Em caso de necessidade de integração de Rastreadores, na tela **"Configurações Gestão Frotas"** (Logística » Gestão de Frotas » Configurações Gestão Frotas), na opção de integração, é necessário entrar em contato com a Operadora de Rastreamento e solicitar a criação de uma conta com perfil de integração.

### Tela - Configurações Gestão de frotas

#### Aba Rastreadores - Configuração da autenticação do Rastreador

Dependendo do tipo de fornecedor, preencha as informações abaixo, habilitando o log em momento de implantação e definindo a quantidade  de dias para armazenamento do histórico de posição.

Para o armazenamento do histórico de integração é recomendado efetuar a análise de acordo com a capacidade de armazenamento e a quantidade de veículos da empresa.

O valor inicial recomendado é de 3 dias.

![Imagem 1: O valor inicial recomendado é de 3 dias.](https://ajuda.sankhya.com.br/hc/article_attachments/33685807469207)

Ao registrar a integração a rotina terá seu processamento a cada 5 minutos. Registrando a posição dos veículos com a latitude e longitude na tabela de dados TCFPOSICAOVEI.

Quando o Flag Registra LOG é habilitado também é registrado o LOG na tabela  TMSLOGINTEGRACAO sobre a autenticação e retorno do XML ou JSON para processamento do dado no Gestão de Frotas.

### Tela - Veículos

Na tela **"Veículos"** (Configurações » Cadastros » Veículos), aba **"TMS"**, selecione o Tipo de Integração do Rastreador e a identificação do Rastreador.

![Imagem 2: Na tela "Veículos" (Configurações » Cadastros » Veículos), aba "TMS" , selecione o Tipo de Integração do Rastreador e a…](https://ajuda.sankhya.com.br/hc/article_attachments/33685540605719)

Após configurada a integração, a rotina executará o JOB de integração a cada 5 minutos.

**Exemplos:**

SELECT \* FROM TCFPOSICAOVEI

![Imagem 3: SELECT * FROM TCFPOSICAOVEI](https://ajuda.sankhya.com.br/hc/article_attachments/33685792530199)

SELECT \* FROM TMSLOGINTEGRAÇÃO

![Imagem 4: SELECT * FROM TMSLOGINTEGRAÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/33685792531479)

**Exemplo de DASH alimentado por esta integração**

![Imagem 5: Exemplo de DASH alimentado por esta integração](https://ajuda.sankhya.com.br/hc/article_attachments/33685807473687)

![Imagem 6: Exemplo de DASH alimentado por esta integração](https://ajuda.sankhya.com.br/hc/article_attachments/33685792534167)
