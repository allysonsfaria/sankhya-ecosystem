---
id: "42430298984727"
titulo: "Ativar Sumarização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430298984727-Ativar-Sumariza%C3%A7%C3%A3o"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:01:32Z"
rotulos: ["sync_hc", "neppo", "neppo_857998347", "sync_hash_ed9d42851cfd"]
---

# Ativar Sumarização

## Visão Geral

Este documento tem como finalidade orientar a ativar o processo de sumarização para uso pela API.

A atualização da sumarização para a memória permanente é realizada diariamente às 02:00am, de forma automatizada uma vez cadastrado o caminho da ativação da sumarização para uso corretamente. Toda configuração é feita uma única vez e só precisa ser alterada em caso de desativação do uso de sumarização.

## Usabilidade

Para cadastrar o caminho da ativação da sumarização para uso, o usuário deverá acessar a funcionalidade disponibilizada NEPPO Vault.

![Imagem 1: Para cadastrar o caminho da ativação da sumarização para uso, o usuário deverá acessar a funcionalidade disponibilizada…](https://ajuda.sankhya.com.br/hc/article_attachments/42639592731927)

Após acessada a funcionalidade, o usuário precisará criar um diretório. Para isso, deverá acionar o botão "Criar diretório", que exibirá uma nova linha.

![Imagem 2: Após acessada a funcionalidade, o usuário precisará criar um diretório. Para isso, deverá acionar o botão "Criar…](https://ajuda.sankhya.com.br/hc/article_attachments/42639582435607)

Na linha exibida, o usuário deverá informar a nomenclatura padrão definida “ia” em minúsculo, e acionar o botão “salvar”.

![Imagem 3: Na linha exibida, o usuário deverá informar a nomenclatura padrão definida “ia” em minúsculo, e acionar o botão…](https://ajuda.sankhya.com.br/hc/article_attachments/42639566484119)

Caso o diretório seja criado com outra nomenclatura, não será reconhecido e acarretará na não identificação da ativação da sumarização. Após criar o diretório, o usuário deverá acionar o ícone "Novo valor", onde será exibido uma interface para preenchimento dos dados de Nome do Valor, Descrição, Formato e Valor.

Depois clique em: “Novo diretório”, e informar a nomenclatura padrão definida “summarization” em minúsculo, e acionar o botão “salvar”.

![Imagem 4: Depois clique em: “Novo diretório”, e informar a nomenclatura padrão definida “summarization” em minúsculo, e acionar o…](https://ajuda.sankhya.com.br/hc/article_attachments/42639593820823)

No campo “Nome do valor” usuário deverá informar o nome padrão definido "active" em minúsculo e no campo "Formato" deverá ser selectionado o “Boolean” e no campo “Valor” deverá ser selecionada a opção “Verdadeiro” como mostra na imagem abaixo:

![Imagem 5: No campo “Nome do valor” usuário deverá informar o nome padrão definido "active" em minúsculo e no campo "Formato"…](https://ajuda.sankhya.com.br/hc/article_attachments/42639610807575)

Encerrado o preenchimento, o usuário deverá acionar o botão “Salvar” finalizando o cadastro da ativação do processo de sumarização.

Por default, o período considerado para criação da memória temporária é de 10 dias, caso queira alterar este período basta configurar também no Neppo Vault, além do path mencionado acima: `/ia/summarization/active`, basta configurar também o caminho: `/ia/summarization/daysreprocess`

![Imagem 6: Por default, o período considerado para criação da memória temporária é de 10 dias, caso queira alterar este período…](https://ajuda.sankhya.com.br/hc/article_attachments/42639567729559)

Caso o período não seja cadastrado, o valor default será adotado automaticamente.
