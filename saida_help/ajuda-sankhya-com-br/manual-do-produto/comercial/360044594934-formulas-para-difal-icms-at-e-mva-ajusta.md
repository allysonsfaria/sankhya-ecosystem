---
id: "360044594934"
titulo: "Fórmulas para DIFAL, ICMS AT e MVA Ajustada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594934-F%C3%B3rmulas-para-DIFAL-ICMS-AT-e-MVA-Ajustada"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:20:15Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Fórmulas", "br.com.sankhya.mgecom.formuladifaliquota", "Fórmula Diferencial de Alíquota manual", "ICMS", "Impostos", "Preferências", "Fórmula Diferencial de Alíquota / Base de ICMS AT", "Comercial"]
---

# Fórmulas para DIFAL, ICMS AT e MVA Ajustada

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311754592663) Módulo: Comercial > Arquivo > Cadastros > Alíquotas
```

---

Utiliza-se esta tela para criar uma fórmula personalizada que será responsável pelo cálculo do diferencial de alíquota de ICMS da empresa.

![Imagem 2: Utiliza-se esta tela para criar uma fórmula personalizada que será responsável pelo cálculo do diferencial de alíquota…](https://ajuda.sankhya.com.br/hc/article_attachments/27444056502167)

Para ativar esta rotina, deve-se acionar a opção **"Calcular ICMS Antecipado Entrada Interestaduais"** presente na aba [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abageraoicmsipi) nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893). Além disso, caso as opções existentes na tela [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934), aba [ICMS Antecipado Entradas Interestaduais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abaicmsantecipadoentradasinterestaduais) estejam configuradas para a aplicação de cálculo do tributo, não será necessário utilizar essa rotina.

**Notas:**

- Ao lançar a nota, lembre-se de incluir os campos na TGFITE visualizada pela Central de Compras, assim, o valor é calculado apenas depois da confirmação da nota.
- Só haverá o preenchimento na tabela TGFDIN se a base de diferencial de ICMS for maior que zero e alíquota maior que zero ou se não estiver usando fórmula no cálculo.
