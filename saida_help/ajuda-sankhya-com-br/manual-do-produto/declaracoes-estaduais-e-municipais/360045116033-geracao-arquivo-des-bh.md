---
id: "360045116033"
titulo: "Geração Arquivo DES-BH"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116033-Gera%C3%A7%C3%A3o-Arquivo-DES-BH"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > Declarações estaduais e municipais"
atualizado_em: "2026-09-15T17:38:33Z"
rotulos: ["AJUDA DO SKW", "manual", "ISS", "Configuração", "Geração", "Arquivo", "Financeiro", "Belo Horizonte", "DES-BH", "br.com.sankhya.mgeliv.mov.geracaoarquivodesbh", "Geração Arquivo DES-BH manual", "Prefeituras", "Competência Baixa tipos de data p/ busca", "Habilitar parâmetro definir versão selecionar empresa", "TOP p/ Serviço Período Dia Pagamento ISS"]
---

# Geração Arquivo DES-BH

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313076840727) Módulo: Livros Fiscais > Conexão
```

---

Por meio desta rotina, será realizada a geração do arquivo para importação da **"DES - Declaração Eletrônica de Serviços"**. A DES é uma declaração mensal de serviços prestados e/ou tomados de qualquer natureza do município de Belo Horizonte - MG.

**Importante:** para utilizar esta tela é necessário habilitar o parâmetro **"Descrição do INFDESBH para DESBH - INFDESBH"** na tela de [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834). A abreviação INFDESBH corresponde à **"Informações do Demonstrativo de Serviço de Belo Horizonte"**.

![Imagem 2: Importante: para utilizar esta tela é necessário habilitar o parâmetro "Descrição do INFDESBH para DESBH - INFDESBH" na…](https://ajuda.sankhya.com.br/hc/article_attachments/26834318355479)

Informe no campo **"Versão do DES"**, a versão de acordo com o layout que está sendo gerada pela empresa.

Defina também a **"Empresa"** da qual será feita a busca dos dados para geração do demonstrativo.

Selecione no campo **"TOP p/ Serviço"**, uma TOP cujo tipo de movimento seja **"Financeiro"**. Os lançamentos realizados diretos na tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874), que fizerem parte do DESBH, deverão ser lançados utilizando a TOP aqui informada.

Determine em **"Período"**, o intervalo de tempo correspondente à geração dos dados do demonstrativo.

Deve ser informado em **"Dia Pagamento do ISS"**, a data que o ISS deve ser recolhido aos cofres municipais.

No campo **"Tipo de Geração"** teremos as seguintes opções disponíveis:

- **Competência:** Quando esta opção for selecionada, o sistema considerará a data de inclusão das notas fiscais.
- **Baixa:** Por meio desta opção, o sistema buscará apenas as notas do período informado, considerando o pagamento/baixa destas.

**Nota:** com esta opção selecionada, a empresa conseguirá realizar a Apuração do ISS e a Geração do Arquivo DES-BH seguindo a exigência do fisco de acordo com o Decreto nº 11.956, art 8º, considerando o período das baixas/pagamentos das Notas Fiscais de Serviços.

Defina no campo **"Tipo de data p/ busca das notas fiscais de serviço"** se a busca das NFS-e's serão de acordo com a **"Dt. Negociação"**, **"Dt. Entrada/Saída"**, **"Dt. Faturamento"** ou conforme a **"Dt. Movimento"**.

Desta forma, o valor do campo 3 do **"Registro R"** dependerá da opção selecionada neste campo.

Depois de definidas as informações, ao acionar o botão ![Imagem 3: Depois de definidas as informações, ao acionar o botão "Gerar arquivo" , é apresentado o pop-up "Processos" contendo as…](https://ajuda.sankhya.com.br/hc/article_attachments/4416260423319) **"Gerar arquivo"**, é apresentado o pop-up **"Processos"** contendo as grades **"Parâmetros de entrada"** e **"Andamento"** da geração do arquivo.

![Imagem 4: Depois de definidas as informações, ao acionar o botão "Gerar arquivo" , é apresentado o pop-up "Processos" contendo as…](https://ajuda.sankhya.com.br/hc/article_attachments/26834345071639)

Já o botão ![Imagem 5: Já o botão "Histórico de Gerações" exibe também o pop-up Processos , mas neste caso, direcionado às gerações já…](https://ajuda.sankhya.com.br/hc/article_attachments/4416261930903) **"Histórico de Gerações"** exibe também o pop-up Processos, mas neste caso, direcionado às gerações já efetuadas, onde, você pode observar dados da geração, como Tempo de Execução, o Usuário responsável por fazê-lo, entre outras informações. 

![Imagem 6: Já o botão "Histórico de Gerações" exibe também o pop-up Processos , mas neste caso, direcionado às gerações já…](https://ajuda.sankhya.com.br/hc/article_attachments/26834318365847)

Ao clicar no botão ![Imagem 7: Ao clicar no botão "Excluir Processos Antigos" no pop-up Processos , o sistema exibirá uma mensagem de confirmação. Ao…](https://ajuda.sankhya.com.br/hc/article_attachments/26834372122519)**"Excluir Processos Antigos"** no pop-up Processos, o sistema exibirá uma mensagem de confirmação. Ao clicar em **"Sim"**, além de remover os registros no pop-up, os arquivos correspondentes também serão excluídos da tela [Repositório de Arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596594-Reposit%C3%B3rio-de-Arquivos). Ao clicar em **"Não"**, nenhuma exclusão será realizada.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116033-Gera%C3%A7%C3%A3o-Arquivo-DES-BH#top)
