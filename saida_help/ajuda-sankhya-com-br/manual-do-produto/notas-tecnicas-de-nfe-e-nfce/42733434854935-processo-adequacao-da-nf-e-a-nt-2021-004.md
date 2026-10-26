---
id: "42733434854935"
titulo: "Processo Adequação da NF-e à NT 2021.004 (v1.10 e v1.30)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42733434854935-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2021-004-v1-10-e-v1-30"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
rotulos: ["NT 2021.004"]
---

# Processo Adequação da NF-e à NT 2021.004 (v1.10 e v1.30)

**Caminhos de Acesso:** Menu Principal › Preferências › Empresa › aba NF-e/NFC-e › sub-aba Nota Técnica NF-e

---

## O que é e para que serve

A Nota Técnica 2021.004 trata das novas regras de validação e das atualizações das regras existentes da NF-e/NFC-e versão 4.0.

Foram incluídos os seguintes campos:

- Grupo Observações de uso livre do Fisco;
- Campo Tipo do Ato Concessório no Grupo de Informações Adicionais da NF-e.

---

#### Configurações necessárias

Ligue os parâmetros **"Gerar tag obsItem no XML da NF-e conf. NT 2021.004-GERATAGOBSITEM"** e **"Envia Observação padrão na NFe-ENVOBSPADNFE"** para ativar a nova geração das observações, conforme a NT 2021.004.

Na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba [Nota Técnica NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#AbaNotaT%C3%A9cnicaNF-e), ative as Notas Técnicas. Ressaltamos que, caso você não cadastre nenhuma nota técnica nesta aba, o sistema irá considerar a informação do campo **"Versão NT"** da aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abanf-enfc-e).

## O que foi alterado

Ao selecionar apenas a opção **Nota Técnica 2021.004 - v1.10** ou apenas a **Nota Técnica 2021.004 - v1.30**, o sistema emite uma mensagem informando que ambas precisam ser configuradas para a correta geração das tags. Com as duas opções definidas, as informações da aba NF-e/NFC-e deixam de ser consideradas.

Emita uma nota fiscal na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), preenchendo os campos **"Observação da ITE"** e **"Observação Padrão"**, sendo esse segundo campo, configurado anteriormente na tela [Observações para Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596474-Observa%C3%A7%C3%B5es-para-Notas).

Na tela [Processos Administrativos Judiciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608094), cadastre um novo processo judicial. Sendo que, na seção **"Configurações XML NF-e"**, deve-se acionar a marcação **"Gerar Tag's do grupo procRef no XML da NF-e"** e selecionar no campo **"Origem do Processo"**, a opção **"0-SEFAZ"**. Informe também o campo **"Tipo do ato concessório"**, de acordo com as opções:

- 08=Termo de Acordo;
- 10=Regime Especial;
- 12=Autorização específica.
