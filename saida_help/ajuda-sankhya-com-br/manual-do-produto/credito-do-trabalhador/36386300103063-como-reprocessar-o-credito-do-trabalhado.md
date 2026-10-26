---
id: "36386300103063"
titulo: "Como reprocessar o Crédito do Trabalhador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36386300103063-Como-reprocessar-o-Cr%C3%A9dito-do-Trabalhador"
trilha: "Manual do Produto > Pessoas+ > Crédito do Trabalhador"
atualizado_em: "2026-10-02T15:52:29Z"
rotulos: ["Atualização", "Importação", "eSocial", "Folha de Pagamento", "Pessoal+", "Crédito do Trabalhador"]
---

# Como reprocessar o Crédito do Trabalhador

**Módulo:** Pessoal+
**Versão:** 5.56.6
**Caminho de acesso:** Pessoal+ > Rotinas Folha
**ID da Tela:**br.com.sankhya.rh.MovimentacoesFolha

---

A partir da versão **5.56.6**, o Pessoal+ disponibilizou o **reprocessamento do Crédito do Trabalhador** por meio da tela Lançamento de Movimentos.

Essa funcionalidade deve ser utilizada quando, ao **calcular a folha**, **liberar a folha para o eSocial** ou **gerar os eventos de pagamento (S-1200/S-2299/S-2399)**, o sistema **não localizar as informações do eConsignado** para a referência.

O reprocessamento garante que os dados do Programa Crédito do Trabalhador sejam atualizados corretamente antes do envio ao eSocial.

### Como utilizar o reprocessamento

**(1)**  **Atualize** o módulo do **Pessoal+** para a versão **5.56.6**.

Somente após essa versão a funcionalidade estará disponível.

**(2)** Acesse a tela **Lançamento de Movimento** (Pessoal+ > Rotinas Folha > Lançamento de Movimento).

**2.1** Selecione a opção **Por funcionário**.

![Imagem 1: 2.1 Selecione a opção Por funcionário .](https://ajuda.sankhya.com.br/hc/article_attachments/36387048512791)

**2.2** Indique a **empresa** e a **referência** (mês/ano) e, clique no ícone **Acertar Importação Crédito Trabalhador**. Será exibida um pop-up para seleção do arquivo do Emprega Brasil. Escolha o arquivo e confirme a importação.

[GIF animado: Imagem 2: 2.2 Indique a empresa e a referência (mês/ano) e, clique no ícone Acertar Importação Crédito Trabalhador . Será exibida…](https://ajuda.sankhya.com.br/hc/article_attachments/36387385862935)

**2.3** Após finalizar a importação, o sistema exibirá uma mensagem informando se o processo foi concluído com sucesso ou se houve algum erro.

![Imagem 3: 2.3 Após finalizar a importação, o sistema exibirá uma mensagem informando se o processo foi concluído com sucesso ou…](https://ajuda.sankhya.com.br/hc/article_attachments/36387515439895)

**(3)** Após importar novamente o arquivo:

- recalcule a folha, **ou**
- faça a liberação da folha ao eSocial, **ou**
- gere novamente os eventos **S-1200**, **S-2299** e/ou **S-2399**.

Depois, envie os eventos pela **Central do eSocial** (Pessoal+ > Rotinas Folha > Central do eSocial).
