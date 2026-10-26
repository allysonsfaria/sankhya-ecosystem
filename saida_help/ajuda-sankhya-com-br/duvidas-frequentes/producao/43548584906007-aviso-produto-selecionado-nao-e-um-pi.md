---
id: "43548584906007"
titulo: "Aviso: Produto selecionado não é um PI."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548584906007-Aviso-Produto-selecionado-n%C3%A3o-%C3%A9-um-PI"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-09-22T15:22:01Z"
rotulos: ["Artigo criado KCS", "Produção - KCS"]
---

# Aviso: Produto selecionado não é um PI.

Quando um **"Produto Intermediário"** (PI) não é reconhecido na composição de um **PA (Produto Acabado)**, mesmo estando corretamente cadastrado com sua composição, é necessário revisar alguns pontos do cadastro. Este cenário pode ocorrer mesmo que as configurações estejam idênticas entre produtos similares e funcional.

![Imagem 1: Quando um "Produto Intermediário" (PI) não é reconhecido na composição de um PA (Produto Acabado) , mesmo estando…](https://ajuda.sankhya.com.br/hc/article_attachments/43589223352343)

### Como corrigir o não reconhecimento do produto intermediário

Para solucionar o problema do PI não reconhecido na composição, siga o procedimento abaixo:

**(1)** Acesse a tela de **"Composição do Produto"** (Produção » Cadastros » Composição do Produto) e valide se aquele produto intermediário tem composição cadastrada. Caso positivo, localize o produto acabado que está com o **PI (Produto Intermediário)** que não está sendo reconhecido.

**Observação:** Se o PI não tiver composição, o sistema não irá conseguir reconhecer que é um produto intermediário.

**(2)** Acessando a composição do PA (Produto Acabado) que está com o problema, será necessário remover o **"Produto Intermediário"** da composição do produto.

**(3)** Inclua novamente o mesmo PI na composição, garantindo que o cadastro do item esteja correto.

**(4)** Salve as alterações. 

**(5)** Para validar, ao clicar no botão "**Outras Opções (...)"**, em seguida **"Configurações do PI",** o sistema irá apresentar o pop-up para configuração do mesmo. Desta forma o sistema já consegue identificá-lo como um **PI (Produto Intermediário).**

![Imagem 2: (5) Para validar, ao clicar no botão " Outras Opções (...)" , em seguida "Configurações do PI", o sistema irá…](https://ajuda.sankhya.com.br/hc/article_attachments/43589223355415)

Este procedimento força o sistema a atualizar o vínculo do PI na tabela de PIs **(TPRLPI),** reconhecendo-o corretamente como **"Produto Intermediário"** na composição.

Pode acontecer de não reconhecer como um **PI**, pois foi incluído como **Matéria Prima** antes de criar o cabeçalho como um **Produto Acabado**.

### Cuidados ao editar composições com ordens lançadas

Se já houver **"Ordens de Produção"** lançadas para a versão atual do processo produtivo, o sistema pode impedir a edição direta da composição, apresentando a mensagem:

**"[PROD\_E00266]: Não é permitido edição, pois já existem Ordens de Produção lançadas para este Processo Produtivo. Crie uma nova versão para realizar edição."**

Neste caso, siga uma das alternativas abaixo:

**(1)** Habilite os parâmetros **"Permitir edição de MPs na composição dos produtos - PERMITEDITMP"** e **"Permitir edição da lista de MPs - PERMITEDITLSTMP"** na tela **"Preferências"** (Configurações » Avançado » Preferências), caso deseje editar sem versionar.

**(2)** Caso prefira manter o controle de versões, crie uma nova versão do processo produtivo para realizar a alteração.

### Boas práticas para manutenção de composições

Sempre que for necessário alterar a composição de um produto, especialmente envolvendo **"Produtos Intermediários"**, siga estas recomendações:

**(1)** Verifique se o cadastro do PI está correto e classificado adequadamente, criando primeiro ser cabeçalho como Produto Intermediário e depois vincular como Matéria Prima no Produto Acabado.

**(2)** Ao remover e adicionar novamente o PI, valide se o sistema reconheceu o vínculo na composição.

**(3)** Evite alterações diretas em composições com **"Ordens de Produção"** já lançadas; prefira versionar o processo produtivo.

Seguindo essas orientações, o sistema irá reconhecer corretamente os **"Produtos Intermediários"** nas composições, evitando falhas no planejamento e execução das **"Ordens de Produção"**.
