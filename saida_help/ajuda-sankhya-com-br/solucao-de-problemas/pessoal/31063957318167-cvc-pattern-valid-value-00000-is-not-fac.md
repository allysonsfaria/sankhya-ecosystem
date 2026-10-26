---
id: "31063957318167"
titulo: "cvc-pattern-valid: Value '00000* is not facet-valid with respect to pattern rd(6)' for type TS-regANS: cvce-type.3.1.3: The value /00000* of element 'regANS is not valid."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31063957318167-cvc-pattern-valid-Value-00000-is-not-facet-valid-with-respect-to-pattern-rd-6-for-type-TS-regANS-cvce-type-3-1-3-The-value-00000-of-element-regANS-is-not-valid"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:19:26Z"
rotulos: ["Configuração", "eSocial", "cvc-pattern-valid", "Value '00000* is not facet-valid with respect to pattern rd(6)", "regANS: cvce-type.3.1.3", "Erro", "Central de Projetos", "Reg ANS"]
---

# cvc-pattern-valid: Value '00000* is not facet-valid with respect to pattern rd(6)' for type TS-regANS: cvce-type.3.1.3: The value /00000* of element 'regANS is not valid.

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31284209031063) MENSAGEM:**

cvc-pattern-valid: Value '00000\* is not facet-valid with respect to pattern rd(6)' for type TS-regANS: cvce-type.3.1.3: The value /00000\* of element 'regANS is not valid.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31284209034263) SITUAÇÃO:**

Ao tentar enviar o evento S1210 no eSocial.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31284209037463) SOLUÇÃO:**

![Imagem 4: Acesse a tela "Plano de Saúde" (Pessoal+ » Cadastros » Plano de Saúde) e verifique o campo "Reg. Ag. Nac. Saúde" , se…](https://ajuda.sankhya.com.br/hc/article_attachments/31284166125591) Acesse a tela **"Plano de Saúde"** (Pessoal+ » Cadastros » Plano de Saúde) e verifique o campo **"Reg. Ag. Nac. Saúde"**, se estiver com quantidade maior que 6 dígitos, faça a devida correção;

![Imagem 5: Após a correção, faça uma nova geração dos eventos do eSocial.](https://ajuda.sankhya.com.br/hc/article_attachments/31284209040535) Após a correção, faça uma nova geração dos eventos do eSocial.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31284166128151) CAUSA:**

Registro na Agência Nacional de Saúde - ANS precisa conter um número de registro válido. Sendo que o tamanho máximo permitido é de 6 dígitos.
