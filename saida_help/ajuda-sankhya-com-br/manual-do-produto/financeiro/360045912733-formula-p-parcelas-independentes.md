---
id: "360045912733"
titulo: "Fórmula p/ Parcelas Independentes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045912733-F%C3%B3rmula-p-Parcelas-Independentes"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:45:43Z"
rotulos: ["Configuração", "Fórmulas", "SEFAZ", "GNRE", "Financeiro", "br.com.sankhya.fin.cad.formula.parcelas.independentes", "Configurar fórmulas por UF e Tipo de Título", "Gerar GNRE com base em fórmulas específicas e campos preenchidos", "Ajustes para GNRE DIFAL e GNRE FCP dependendo da fórmula"]
---

# Fórmula p/ Parcelas Independentes

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312529336087) Módulo: Financeiro > Arquivos > Cadastros > Tipos de Título
```

---

Como já se sabe, os valores dos financeiros que serão gerados são influenciados pelo campo **"Fórmula"** da tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas).

Além disso, é possível configurar fórmulas específicas para parcelas independentes, levando em conta a UF (estado) e o Tipo de Título.

No entanto, é importante ressaltar que quando houver uma **"Fórmula para Parcelas Independentes"**, os cálculos de vencimento das parcelas do título serão desconsiderados. Neste caso, os vencimentos serão definidos com base apenas na fórmula configurada.

![Imagem 2: No entanto, é importante ressaltar que quando houver uma "Fórmula para Parcelas Independentes" , os cálculos de…](https://ajuda.sankhya.com.br/hc/article_attachments/27404394962839)

 É fundamental que todas as fórmulas estejam corretas, pois qualquer erro impedirá a geração do financeiro na Central de Vendas e comprometerá diretamente a rotina de emissão das Notas Fiscais (NFs). Revise cuidadosamente antes de salvar!

Desta forma, caso a fórmula não esteja preenchida na tela Tipos de Negociação e exista um registro nesta tela de Fórmula p/ Parcelas Independentes que possua o **"Tipo de Título"** como Nota Fiscal e a **"UF"** como Minas Gerais, a fórmula que prevalecerá e será considerada é a que foi informada no campo Fórmula desta última rotina citada.

Após checar os financeiros da nota gerada, pode-se observar que apenas os Tipos de Título igual a Nota Fiscal terão um valor diferente, devido a configuração realizada na tela Fórmulas p/ Parcelas Independentes, de acordo com o que explicamos acima.

Após isto, na tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela), aba **"GNRE"**, você poderá visualizar a informação da chave de acesso da nota, preenchida no campo **"Chave de acesso NFe"**.

O campo **"Código GNRE"** buscará os cadastros realizados para aquela UF, na tela [Estados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294-Estados), sub-aba **"GNRE Unidade Federativa"**.

**Observação:**

O sistema irá gerar a GNRE para o parceiro vinculado na Fórmula para Parcelas Independentes quando o campo indicado estiver preenchido com um valor, por exemplo, se for indicado que o valor da fórmula será pertinente ao campo VLRICMSDIFALDEST, este deve possuir uma quantidade informada.

Além disso, para que o sistema não gere GNRE para parceiros de estados que não possuem Fórmula para Parcela Independente, o campo Fórmula do Tipo de Negociação não deverá ser preenchido, pois com o campo vazio, o sistema fará a busca da fórmula para parcelas independentes.

No campo **"Código da Receita (GNRE)"** insira o código da receita correspondente ao estado em questão. Esse código é definido pela SEFAZ (Secretaria da Fazenda do Estado).

Preencha o campo **"Código do Produto (GNRE)"** conforme a tabela fornecida pela SEFAZ/UF, respeitando a exigência específica de cada estado.

Através do campo **"Receita ou Despesa"** você pode definir se a parcela independente é Receita, Despesa ou nenhuma. Assim, na tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas), referente ao campo **"Tipo de Título"** informado, será considerada a opção escolhida inicialmente no campo Receita ou Despesa do respectivo Tipo de Título.

**Observação:** ao cadastrar uma regra para o estado do RJ você poderá realizar a geração da GNRE com múltiplas receitas, através dos campos **"Indicador de valor 1"** e **"Indicador de valor 2"** que possuem as seguintes opções:

- Valor Principal ICMS;
- Valor Principal Fundo de Pobreza.

Nessa tela, ainda é possível configurar a guia GNRE DIFAL por UF e Tipo de Título. Desse modo, para que seja considerada a fórmula das parcelas independentes é necessário que quando a opção **"GNRE DIFAL"** estiver selecionada no **"Tipo de Título"** da aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas) da tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173), o campo **"Fórmula"** também desta aba, não seja preenchido. Considere ainda que:

- Quando o campo Fórmula estiver em branco na tela Tipos de Negociação e existir uma **"Fórmula"** na tela Fórmulas p/ Parcelas Independentes, a GNRE DIFAL é calculada corretamente no Financeiro da nota;
- Caso o campo Fórmula da tela Tipos de Negociação esteja com 0 (zero), o sistema não irá recalcular o valor no Financeiro da nota quando ocorrer qualquer alteração na [Grade de Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414).

Exemplo:

Foi inserido o Produto com 1 quantidade na Grade de Itens (valor GNRE DIFAL: R$ 15,37);
Em seguida alterou-se para 2 quantidades (valor GNRE DIFAL deveria ser alterado para R$ 30,73).
O valor da GNRE DIFAL deveria ser recalculado, pois foi alterada a quantidade de itens, mas no Financeiro não é recalculado, é mantido o valor do imposto R$ 15,37.

Ressaltando que, este comportamento ocorre quando o 0 (zero) é utilizado no campo Fórmula da tela Tipos de Negociação do GNRE DIFAL.

Já, no caso da GNRE FCP o comportamento é o inverso. Quando se utiliza as fórmulas de parcelas independentes na tela Tipos de Negociação, aba Parcelas, o Tipo de Título **"GNRE FCP"** precisará ficar com 0 (zero) para que seja considerada a fórmula das parcelas independentes, pois este não possui a particularidade de cálculo e recálculo. Independente do valor e quantidade inseridos, o sistema recalcula conforme o esperado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045912733-F%C3%B3rmula-p-Parcelas-Independentes#top)
