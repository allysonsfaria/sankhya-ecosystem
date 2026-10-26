---
id: "34382742634775"
titulo: "Motivo: javax.ejb.CreateException: SQL-50001 O Centro de Resultado XXXX  não está cadastrado, não está ativo, ou não é analítico"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34382742634775-Motivo-javax-ejb-CreateException-SQL-50001-O-Centro-de-Resultado-XXXX-n%C3%A3o-est%C3%A1-cadastrado-n%C3%A3o-est%C3%A1-ativo-ou-n%C3%A3o-%C3%A9-anal%C3%ADtico"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:20:39Z"
rotulos: ["Configuração", "Movimentação Financeira", "Centro de Resultado", "Financeiro", "Motivo", "SQL-50001", "Gerenciador de Folhas", "Erro", "não é analítico", "javax.ejb.CreateException", "não está cadastrado", "não está ativo", "centro de resultado está inativo", "centro de resultado está correto"]
---

# Motivo: javax.ejb.CreateException: SQL-50001 O Centro de Resultado XXXX  não está cadastrado, não está ativo, ou não é analítico

**MENSAGEM**

Motivo: javax.ejb.CreateException: SQL-50001 O Centro de Resultado XXXX  não está cadastrado, não está ativo, ou não é analítico

**SITUAÇÃO**

A mensagem de erro é apresentada ao tentar realizar a integração financeira da folha de pagamento pela tela **"Gerenciador de Folhas"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas).

**SOLUÇÃO**

Siga as orientações conforme o cenário identificado:

**(1)**  Se o **centro de resultado está inativo** e não será mais utilizado:

- Identifique onde o centro de resultado está cadastrado (exemplo: **"Empresas"**, **"Eventos"**, **"Departamentos"**, **"Rateios"**, entre outros).
- Substitua pelo centro de resultado que deverá ser utilizado a partir de agora.

**(2)**  Se o **centro de resultado está correto**:

- Ative o centro de resultado.
- Marque a opção **"Analítico"** para que a integração seja realizada com sucesso.

**CAUSA**

O erro ocorre quando o centro de resultado informado para a integração financeira está desativado ou não está marcado como analítico.
