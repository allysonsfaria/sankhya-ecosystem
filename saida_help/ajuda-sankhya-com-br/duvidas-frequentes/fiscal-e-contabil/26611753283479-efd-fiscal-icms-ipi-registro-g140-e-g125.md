---
id: "26611753283479"
titulo: "EFD FISCAL - ICMS/IPI - Registro G140 e G125 - Campos vazios causando erros na validação no PVA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26611753283479-EFD-FISCAL-ICMS-IPI-Registro-G140-e-G125-Campos-vazios-causando-erros-na-valida%C3%A7%C3%A3o-no-PVA"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:41:03Z"
rotulos: ["Configuração", "IPI", "ICMS", "Validação", "Impostos", "EFD", "G140 campos 6 ao 9", "Registro G140 e G125 - Campos vazios", "erros na validação no PVA", "G125 campos 5 ao 8"]
---

# EFD FISCAL - ICMS/IPI - Registro G140 e G125 - Campos vazios causando erros na validação no PVA

Estes campos vazios são preenchidos com os valores indicados nos campos: **'Valor do ICMS', 'Valor crédito por subst. tributária', 'Valor crédito de ICMS dif. Alíquota', 'Valor crédito ICMS sobre frete',** existentes na aba **"CIAP",** do cadastro do BEM imobilizado ativado, quando o produto atualiza CIAP.

Acontece que se nestes campos citados acima não existem valores informados, o sistema ao gerar o registro G125 e G140, ao invés de preencher com zeros, deixa-os em branco, o que ocasiona o erro apontado pelo PVA do EFD ICMS.

**G125 campos 5 ao 8**

**G140 campos 6 ao 9**

Para que na geração o sistema deixe de gerar os referidos campos vazios e gere com o valor **zero**, ative o parâmetro **"GERCAMZERBLCG"**, assim serão cessados os erros no validador.
