---
id: "37313674487703"
titulo: "1000 Rejeição: Município do Fato Gerador do IBS só pode ser informado em operação presencial fora do estabelecimento (indPres = 5)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37313674487703-1000-Rejei%C3%A7%C3%A3o-Munic%C3%ADpio-do-Fato-Gerador-do-IBS-s%C3%B3-pode-ser-informado-em-opera%C3%A7%C3%A3o-presencial-fora-do-estabelecimento-indPres-5"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:13:29Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "TOP", "indPres", "Municipio do fato gerador do IBS", "Presencial fora do estabelecimento", "cMunFGIBS", "Indicador de Presença para NF-e/NFC-e/CF-e"]
---

# 1000 Rejeição: Município do Fato Gerador do IBS só pode ser informado em operação presencial fora do estabelecimento (indPres = 5)

**MENSAGEM:**

1000 Rejeição: Município do Fato Gerador do IBS só pode ser informado em operação presencial fora do estabelecimento (indPres = 5).

**SOLUÇÃO:**

**(1)** Acesse a tela [**''Tipos de Operação''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(2)** Selecione a TOP utilizada na NF-e rejeitada.

**(3)** Na aba **''NF-e/NFC-e/CF-e''** no campo **''Indicador de Presença para NF-e/NFC-e/CF-e''** configure como ''**5 – Presencial, fora do estabelecimento''**.

- Somente se a operação realmente ocorrer nessa modalidade.

**(4)** Caso a operação **não seja presencial fora do estabelecimento**,  não deve ser informado **cMunFGIBS**.

Nesse caso:

- Ajuste a regra ou personalização que esteja preenchendo esse campo de forma indevida;
- Remova o preenchimento do município do fato gerador do IBS.

**(5)** Salve as alterações e transmita novamente a NF-e.

##### CAUSA:

Essa rejeição ocorre quando o município do fato gerador do IBS (**cMunFGIBS**) é preenchido no XML da NF-e, porém a operação não está configurada como **presencial fora do estabelecimento** (indPres diferente de 5), gerando inconsistência nas validações da SEFAZ.
