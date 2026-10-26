---
id: "39290297576855"
titulo: "Salário Família não sendo calculado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39290297576855-Sal%C3%A1rio-Fam%C3%ADlia-n%C3%A3o-sendo-calculado"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:31Z"
rotulos: ["Configuração", "Impostos", "Dependentes", "Folha de Pagamento", "Artigo criado KCS", "Sankhya RH - KCS", "Salário Família"]
---

# Salário Família não sendo calculado

**SITUAÇÃO**

O sistema apresenta não calcula salário família para colaboradores que possuem direito ao benefício. Esta ocorrência impacta a folha de pagamento, gerando inconsistências nos valores calculados.

**CAUSA**

A causa raiz desta inconsistência está geralmente associada a configurações incorretas  ou falhas na atualização da tabela de **"Salário Família"**  . O sistema pode estar considerando parâmetros de vencimentos indevidos ou não processando corretamente o limite de renda mensal do colaborador.

## Como funciona o cálculo do Salário-Família

O sistema calcula o salário-família com base em:

✅ **Dependentes cadastrados** - Filhos ou equiparados dentro da faixa etária permitida

✅ **Limite salarial** - O colaborador deve estar dentro do teto de remuneração vigente

✅ **Tabela de faixas** - Valores da cota definidos pela legislação para cada competência

✅ **Dias trabalhados** - O valor é proporcional aos dias efetivamente trabalhados no mês

**SOLUÇÃO**

Para corrigir o cálculo, siga os passos abaixo:

Acesse a tabela de faixa **"Salário Família"** (Pessoal+ » Cadastros » Tabela de Faixas) e verifique se os limites de renda e valores do benefício estão atualizados conforme a tabela oficial do governo.

![Imagem 1: Acesse a tabela de faixa "Salário Família" (Pessoal+ » Cadastros » Tabela de Faixas) e verifique se os limites de renda…](https://ajuda.sankhya.com.br/hc/article_attachments/41123591716887)

Verifique na tela **"Dependentes"** (Pessoal+ » Cadastros » Configuração Funcionários) se o campo **"Dependente de Salário Família"** está marcado para o colaborador /dependente em questão.

![Imagem 2: Verifique na tela "Dependentes" (Pessoal+ » Cadastros » Configuração Funcionários) se o campo "Dependente de Salário…](https://ajuda.sankhya.com.br/hc/article_attachments/41123559061399)

⚠️ **Importante:** A opção **"Filho(a)/Enteado(a) Incapaz"** não concede direito ao salário-família, pois o sistema o interpreta como enteado.

Consulte a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos) e certifique-se de que o evento relacionado ao salário família está ativo, se possui a incidência correta e as fórmulas de cálculo não foram alteradas manualmente.

Após realizar as conferências, acesse a tela **"Cálculo da Folha"** (Pessoal+ » Rotinas Folha » Cálculos) e refaça o cálculo do colaborador para que o sistema atualize as verbas com base nas correções efetuadas.
