---
id: "32877929658647"
titulo: "Campo deve ser preenchido quando o registro 0010, campo forma_trib, for igual a 8 ou 9 (Imune ou Isento de IRPJ)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32877929658647-Campo-deve-ser-preenchido-quando-o-registro-0010-campo-forma-trib-for-igual-a-8-ou-9-Imune-ou-Isento-de-IRPJ"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:30:05Z"
rotulos: ["Configuração", "Relatórios", "Empresa", "ECF", "Impostos", "Contabilidade", "erro", "0010", "forma_trib", "FORMA_APUR_I"]
---

# Campo deve ser preenchido quando o registro 0010, campo forma_trib, for igual a 8 ou 9 (Imune ou Isento de IRPJ)

**MENSAGEM:**

Erro apresentado no relatório da ECF: Campo deve ser preenchido quando o registro 0010, campo forma\_trib, for igual a 8 ou 9 (Imune ou Isento de IRPJ).

**SOLUÇÃO:**

Acesse a tela **''Empresa''** (Contabilidade> Preferências), aba '**'ECF- Escrituração Contábil Fiscal''** e sub-aba **''Parâmetros de tributação''**.

**(1)** O campo **''Apuração do IRPJ para Imunes ou Isentas''** só deve ser preenchido quando o campo **''Forma de tributação''** for **imune ou isenta.**

![Imagem 1: (1) O campo ''Apuração do IRPJ para Imunes ou Isentas'' só deve ser preenchido quando o campo ''Forma de tributação''…](https://ajuda.sankhya.com.br/hc/article_attachments/33154446860951)

**AMBIENTE E CAUSA DO ERRO:** 

**Registro com erro**: 0010 

**Campo com erro**: FORMA\_APUR\_I

**Conteúdo atual**: O campo Apuração do IRPJ para Imunes ou Isentas está com valor **D**, mas **não deveria.** Pois, ele deve ser preenchido **somente quando a Forma de tributação, no campo forma\_trib, estiver igual a 8 ou 9.**
