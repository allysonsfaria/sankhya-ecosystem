---
id: "4403127493143"
titulo: "Cadastro Massivo de Endereços"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403127493143-Cadastro-Massivo-de-Endere%C3%A7os"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:16:45Z"
rotulos: ["Configuração", "WMS", "Atualização", "Estoque", "Endereços", "br.com.sankhya.wms.CadastroMassivoEnderecoWMS", "MASCENDWMS", "Cadastro", "Configurações detalhadas: Grau analítico atributos do endereço", "Geração automática de endereços: Simplificação do cadastro", "Opção de atualização massiva: Facilita a edição"]
---

# Cadastro Massivo de Endereços

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311654955927) Módulo: WMS > Cadastros            ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42311654959383) Versão disponível: A partir da versão 4.8
```

---

Nessa tela, você poderá realizar a geração automática de endereços inserindo as informações necessárias para a criação da hierarquia do armazém que será utilizado nos seus processos, dessa forma, isso poupará tempo no momento do cadastro dos endereços.

![Imagem 3: Nessa tela, você poderá realizar a geração automática de endereços inserindo as informações necessárias para a criação…](https://ajuda.sankhya.com.br/hc/article_attachments/4405640037399)

No campo **"Empresa"** dessa tela, insira a empresa onde o cadastro dos endereços será realizado. Aqui, serão apresentadas apenas as empresas controladas pelo WMS.

Em **"Grau de nível analítico"**, determine o grau analítico do armazém, conforme a máscara definida.

Os graus a serem exibidos nessa tela, deverão seguir o configurado na tela [Máscara para Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120513).

**Observação:** se a máscara for informada na tela Máscara para Endereço de Armazenamento antes de configurá-la no parâmetro **"Máscara para Endereços WMS - MASCENDWMS"**, este será automaticamente preenchido com o que foi configurado na tela mencionada anteriormente.

---

**Seção Configurações para grau analítico**

Nessa seção, você irá adicionar as informações referentes à **"Altura"**, **"Largura"**, **"Profundidade"** e **"Peso Máximo"**. Além das seguintes marcações:

Em **"Ativo"**, será definido se o endereço em questão estará ativo ou não ativo para uso.

Você deve habilitar a marcação **"Multi produto"** para o endereço que possuir produtos com a marcação **"Multi produto"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral) da tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento) selecionada. Caso contrário, o produto em questão deve estar cadastrado na aba [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abaproduto) da tela Endereço de Armazenamento.

A marcação **"Picking"** deve ser selecionada se o endereço for reconhecido como picking.

A opção **"Permite expedição"** indicará se o endereço permitirá ou não expedições a partir dele.

Em **"Reabastecido por Picking"**, você indicará se o endereço será ou não reabastecido por picking.

Ao selecionar a marcação **"Lote Único"** nos endereços, não será permitida a inserção de mais de um lote por produto no endereço correspondente, porém você poderá inserir mais de um produto desde que o endereço esteja com a configuração Multi Produto feita.

A marcação **"Permite Fragmentar Estoque"** deve ser realizada em endereços onde é permitido pegar partes do estoque existente, como por exemplo, Picking.

Ao realizar a marcação **"Usa picking intermediário"** será indicado que este é um endereço cujas tarefas devem levar a um picking intermediário.

A marcação **"Picking Intermediário"** indica que o endereço em questão, é um picking intermediário.

---

No botão **"Outras Opções..."** dessa tela, temos disponível a opção **"Atualização Massiva de Endereço"** em que, ao clicar nesta, o sistema abrirá o pop-up de mesmo nome onde você poderá realizar edições dos endereços criados anteriormente nessa tela, uma vez que estas serão refletidas nos endereços disponíveis na tela Endereço de Armazenamento.

![Imagem 4: No botão "Outras Opções..." dessa tela, temos disponível a opção "Atualização Massiva de Endereço" em que, ao clicar…](https://ajuda.sankhya.com.br/hc/article_attachments/4405646591895)

No pop-up, temos um painel de filtros onde você poderá utilizar para filtrar os endereços que deseja editar, neste temos:

No campo **"Faixa de endereços"** e **"a"** informe os endereços que serão filtrados como, por exemplo, para editar os endereços 1,2 e 3, insira 1 no campo Faixa de endereços e 3 no campo a.

Em **"Lado"**, você pode selecionar uma dentre as opções **"Ímpar"**, **"Par"** ou **"Todos"**.

Ao clicar em **"Aplicar"**, é possível remover ou não os registros de acordo com suas preferências por meio dos botões ![Imagem 5: Ao clicar em "Aplicar" , é possível remover ou não os registros de acordo com suas preferências por meio dos botões…](https://ajuda.sankhya.com.br/hc/article_attachments/16840361811223) **"Remover selecionados"** e ![Imagem 6: Ao clicar em "Aplicar" , é possível remover ou não os registros de acordo com suas preferências por meio dos botões…](https://ajuda.sankhya.com.br/hc/article_attachments/16840361816727) **"Remover NÃO selecionados"**.

Depois, no painel **"Dados para atualização"** você poderá editar os dados dos endereços filtrados em conjunto.

[GIF animado: Imagem 7: Depois, no painel "Dados para atualização" você poderá editar os dados dos endereços filtrados em conjunto.](https://ajuda.sankhya.com.br/hc/article_attachments/4405646681623)
