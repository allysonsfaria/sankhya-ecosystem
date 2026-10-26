---
id: "32401173681431"
titulo: "(visto Fer) A folha do Autônomo ou do Pró Labore está ficando sem eventos."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32401173681431--visto-Fer-A-folha-do-Aut%C3%B4nomo-ou-do-Pr%C3%B3-Labore-est%C3%A1-ficando-sem-eventos"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:19:50Z"
rotulos: ["Configuração", "Preferências", "Folha", "Autônomo", "folha do Autônomo", "está ficando sem eventos", "tabela de férias (TFPFER) encontra-se vazia para o funcionário", "Pró Labore", "Erro"]
---

# (visto Fer) A folha do Autônomo ou do Pró Labore está ficando sem eventos.

**MENSAGEM:**

Falha - A tabela de férias (TFPFER) encontra-se vazia para o funcionário. Esta é uma configuração inválida dado que na admissão é realizada a inserção do primeiro período aquisitivo do funcionário.

**SITUAÇÃO:**

Essa situação ocorre especificamente quando:

- O trabalhador está cadastrado com vínculo de autônomo ou pró labore, porém, esses vínculos não estão incluídos no parâmetro **FPSEMFERIAS**, que define os vínculos sem direito a férias.
- Como resultado, o sistema interpreta que o autônomo ou pró labore tem direito a férias e, por isso, tenta acessar registros na tabela TFPFER que, nesse caso, está vazia, resultando em erro no processamento.

**SOLUÇÃO:**

Acesse a tela **"Preferências"** (Configurações» Avançado » Preferências) e no **parâmetro FPSEMFERIAS** inclua os vínculos que não têm direito a férias:

- 02 - Estagiário
- 80 - Diretor Sem Vínculo Empregatício
- 90 - Profissional Autônomo
- 99- Pensionistas

![Imagem 1: 99- Pensionistas](https://ajuda.sankhya.com.br/hc/article_attachments/32404395068823)

Após a inclusão correta dos vínculos no parâmetro, o sistema não buscará mais registros de férias para esses vínculos, permitindo que o cálculo da folha seja realizado sem erros.

**CAUSA:**

Ao realizar o cálculo, o sistema tenta localizar um período aquisitivo de férias na tabela **TFPFER**. Esse registro é criado automaticamente no momento da admissão de empregados que têm direito a férias.

No entanto, trabalhadores autônomos ou pró labore não têm direito a férias. Por isso, eles não devem gerar registros na tabela  TFPFER. Se esse tipo de vínculo não for corretamente classificado como **“sem direito a férias”**, o sistema tentará localizar um período aquisitivo que não existe, o que causa uma falha no processamento.
