---
id: "360043697993"
titulo: "Nota 'X' DENEGADA não pode ser Cancelada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043697993-Nota-X-DENEGADA-n%C3%A3o-pode-ser-Cancelada"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:02:41Z"
rotulos: ["#criadoRoger", "Configuração", "NF-e", "SEFAZ", "TOP", "NF-e Denegada não pode ser cancelada", "Verifique status; notas denegadas não são canceláveis", "Cancelamento não permitido para notas denegadas", "Erro", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Nota 'X' DENEGADA não pode ser Cancelada

**MENSAGEM**

**SITUAÇÃO**

A Nota Fiscal Eletrônica foi **denegada pela SEFAZ** em razão de irregularidade fiscal do destinatário. No entanto, o sistema ainda apresenta o status como **“Enviada”**.

Ao tentar excluir, cancelar ou realizar qualquer alteração na nota, a ação é bloqueada pelo sistema, em função do status atual apresentado.

**SOLUÇÃO**

Para resolver este problema, siga os passos abaixo:

**(1)** Certifique-se de que o sistema esteja atualizado para a versão **4.35b243** ou superior. Essa versão contempla a correção do problema em que notas denegadas permaneciam com status incorreto.

**(2)** Além disso, acesse a tela **“Empresa”** (Comercial >> Preferências) e verifique se a **“NT 2024.001”** está devidamente ativa.

![Imagem 1: Na tela "Tipo de Operação - TOP" ( Comercial >> Arquivo >> Cadastros ), localize a TOP utilizada na emissão da nota.…](https://ajuda.sankhya.com.br/hc/article_attachments/39543455291543)

**(3)** Na tela **"Tipo de Operação - TOP"** (Comercial >> Arquivo >> Cadastros), localize a TOP utilizada na emissão da nota.

**(4)** Acesse a aba **"NF-e/NFC-e/CF-e"** e verifique o campo **"Tipo de operação NF-e Denegada".** Caso esteja preenchido remova a TOP Denegada, deixando em branco.

**(5)** Retorne à tela **"Portal de Vendas"** (Comercial >> Consulta) e utilize a opção "**NF-e**" >> **"Consulta situação atual da nota"** para que o sistema atualize corretamente o status conforme o retorno da SEFAZ.

**(5)**Execute as seguintes ações: notifique o parceiro sobre a irregularidade fiscal e, após a devida correção por parte dele, realize a transmissão da NF-e novamente. Caso não deseje prosseguir, é necessário inutilizar a numeração e excluir a nota.

Ressaltamos que notas denegadas não devem ser canceladas. Após mudanças realizadas pela SEFAZ, a nota passará a ser retornada com rejeição, permitindo assim o seu reaproveitamento após a devida correção.

**CAUSA**

Desde agosto de 2024, a SEFAZ alterou o tratamento das notas denegadas. Conforme o Ajuste SINIEF nº 43/2023, o evento de denegação de NF-e foi descontinuado.

Dessa forma, as irregularidades passaram a retornar como **Rejeição 307 – Emitente bloqueado pela UF de destino**, deixando o documento com status **“Aguardando Correção”**.
