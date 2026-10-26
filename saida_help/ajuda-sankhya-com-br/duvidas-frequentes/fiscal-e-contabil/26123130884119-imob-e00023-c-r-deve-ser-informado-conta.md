---
id: "26123130884119"
titulo: "IMOB_E00023 - C.R. deve ser informado. Conta que exige o CR"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26123130884119-IMOB-E00023-C-R-deve-ser-informado-Conta-que-exige-o-CR"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:43:10Z"
rotulos: ["Configuração", "Imobilizado", "Centro de Resultado", "Contabilização", "C.R. deve ser informado. Conta que exige o CR:", "MOB_E00023", "Erro"]
---

# IMOB_E00023 - C.R. deve ser informado. Conta que exige o CR

**![Imagem 1: MENSAGEM : I](https://ajuda.sankhya.com.br/hc/article_attachments/26123130874007) MENSAGEM**: I

MOB\_E00023 - C.R. deve ser informado. Conta que exige o CR

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/26123153793431) SOLUÇÃO**:

Primeiro é preciso entender de qual local o sistema buscará o Centro de Resultado para contabilização da depreciação do bem:

Será do CR informado no "Departamento" que deve ser vinculado ao bem:

![Imagem 3: Será do CR informado no "Departamento" que deve ser vinculado ao bem:](https://ajuda.sankhya.com.br/hc/article_attachments/26400957827863)

![Imagem 4: Será do CR informado no "Departamento" que deve ser vinculado ao bem:](https://ajuda.sankhya.com.br/hc/article_attachments/26400957832087)

(1)** IMPORTANTE:**

Se durante a criação do bem no sistema não foi vinculado um departamento a ele, impossibilitando assim a busca do CR, é possível usar a tela **"Consulta/Movimentação de Bem"**(Caminho: Imobilizado » Rotinas » Consulta/Movimentação de Bem). Nela tem-se a rotina [Transferência de Bem,](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595474-Consulta-Movimenta%C3%A7%C3%A3o-de-Bem#transfer%C3%AAnciadebem) que movimenta o bem entre os departamentos cadastrados no sistema. Porém, é preciso se atentar a ordem **cronológica das movimentações:**

Se for feito o vínculo do bem a um departamento que antes não existia o vínculo, no histórico de movimentação será salvo o **dia e hora** em que foi feita essa ação, histórico esse que pode ser consultado na rotina [Consultar movimentação do bem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595474-Consulta-Movimenta%C3%A7%C3%A3o-de-Bem#consultarmovdobem). 

Dito isto, se estiver contabilizando uma referência **anterior** a essa movimentação de departamento, o sistema continuará não encontrando o Centro de Resultado. Então, ao criar esse vínculo, deve-se usar uma data **retroativa** na rotina Transferência de Bem, que seja suficiente para cobrir a referência/data do movimento de geração do lote que está realizando.

**![Imagem 5: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/26123130875927) CAUSA**:

Durante a execução da rotina **"Geração de Lote de Depreciação",** o sistema busca os valores de depreciação que foram calculados pela rotina **"[Cálculo da Depreciação Mensal"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053497654-C%C3%A1lculo-da-Deprecia%C3%A7%C3%A3o-Mensal)** (Caminho: Imobilizado » Rotinas » Cálculo da Depreciação Mensal) Em seguida, procura as contas contábeis pré-definidas no cadastro **["sub-aba Contas do Produto"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontasdoproduto)** (Caminho: Configurações » Cadastros » Produtos » Produtos) ou **["sub-aba Bens", Contas do bem,](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-ababens)** para gerar o lote contábil de depreciação e alimentar as contas cadastradas.

Nesse momento, se os dados processados pelo sistema não encontrarem o Centro de Resultado para alimentar as contas contábeis citadas no passo anterior, e estas contas estiverem com a marcação "**Centro de Resultado obrigatório"** em cadastro na tela **"Plano de Contas"** (Caminho: Contabilização » Cadastros » Plano de Contas), a mensagem de alerta será apresentada.
