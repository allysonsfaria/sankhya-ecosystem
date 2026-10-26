---
id: "9240384293015"
titulo: "Existe empresa do Simples Nacional cadastrada no sistema e o campo CSOSN não foi configurado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9240384293015-Existe-empresa-do-Simples-Nacional-cadastrada-no-sistema-e-o-campo-CSOSN-n%C3%A3o-foi-configurado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:09:15Z"
rotulos: ["CSOSN", "Configuração", "Simples Nacional", "Impostos", "Alíquotas de ICMS", "CORE_E06608", "Alerta de Configuração de ICMS", "Erro"]
---

# Existe empresa do Simples Nacional cadastrada no sistema e o campo CSOSN não foi configurado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18611523713943) MENSAGEM:**

[CORE\_E06608] Existe empresa do Simples Nacional cadastrada no sistema e o campo CSOSN não foi configurado.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18611549541655) SITUAÇÃO:**

Ao tentar configurar uma alíquota de ICMS que não é Simples Nacional a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18611549552535) CAUSA:**

Quando existe alguma empresa cadastrada como Simples Nacional e o campo CSOSN não estiver preenchido.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18611523735319) SOLUÇÃO:**

A mensagem de alerta é apresentada, a partir das versões mais recentes da 4.11.

Foi feito o processo de melhoria no sistema para que seja feita a validação do CSOSN quando possuir alguma empresa optante do Simples Nacional cadastrada no Sistema.

Portanto as regras de alíquota que foram cadastradas anteriormente precisam ser ajustadas com o preenchimento do campo conforme imagem abaixo:

(Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS)

![Imagem 5: (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS)](https://ajuda.sankhya.com.br/hc/article_attachments/18611549561111)
