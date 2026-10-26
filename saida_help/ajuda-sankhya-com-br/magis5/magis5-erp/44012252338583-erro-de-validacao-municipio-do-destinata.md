---
id: "44012252338583"
titulo: "Erro de validação (Município do destinatário inválido), aguarde nova tentativa de faturamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012252338583-Erro-de-valida%C3%A7%C3%A3o-Munic%C3%ADpio-do-destinat%C3%A1rio-inv%C3%A1lido-aguarde-nova-tentativa-de-faturamento"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:23:29Z"
rotulos: ["sync_hc", "magis5", "sync_hash_df27df4fe6fa", "magis5_204056246809"]
---

# Erro de validação (Município do destinatário inválido), aguarde nova tentativa de faturamento

## Este erro indica que houve um problema com a informação referente ao município do destinatário da nota fiscal.

Para resolver esse erro, você pode considerar as seguintes etapas:

**CONSULTE AS INFORMAÇÕES FISCAIS**

Verifique se o município "Caetano Mendes" está devidamente registrado nos registros fiscais do estado do Paraná (PR) como um município válido.

O primeiro passo para essa validação é identificar o CEP informado no cadastro do cliente, para isso, clique em: Menu → Cadastros → Clientes, insira o nome do cliente no campo de buscas e clique em: Aplicar Filtro:

![Imagem 1: O primeiro passo para essa validação é identificar o CEP informado no cadastro do cliente, para isso, clique em: Menu →…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-2.png)

Clique em: Editar:

![Imagem 2: Clique em: Editar:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-5-1024x317.png)

Em "Endereço Principal", identifique o CEP:

![Imagem 3: Em "Endereço Principal", identifique o CEP:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-4-1024x297.png)

Agora, utilizando o Google ou o próprio site dos [Correios](https://buscacepinter.correios.com.br/app/endereco/index.php), busque o CEP e verifique se o endereço informado pelo cliente coincide com o resultado obtido.

![Imagem 4: Agora, utilizando o Google ou o próprio site dos Correios , busque o CEP e verifique se o endereço informado pelo…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-1.png)

Observações:

1. Muitas vezes, o próprio Artemis5 faz a validação e corrige o endereço no cadastro do cliente;
2. Caso o endereço cadastrado esteja divergente ao informado nos Correios, será necessário editar o cadastro do cliente, alterando-o. Para isso, no cadastro do cliente, faça as correções necessárias e clique em: Salvar.

**CORRIJA O ENDEREÇO DO CLIENTE NA VENDA**

Após a validação do endereço, é necessário "informar" para o Artemis5 que o endereço está corrigido.

Para isso, localize o pedido com erro na tela de vendas e clique em: Corrigir Endereço:

![Imagem 5: Para isso, localize o pedido com erro na tela de vendas e clique em: Corrigir Endereço:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-6-1024x168.png)

Selecione "Endereço Principal" e clique em: Salvar.

![Imagem 6: Selecione "Endereço Principal" e clique em: Salvar.](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-7-1024x388.png)

Aguarde aproximadamente cinco minutos para a venda ser reprocessada e faturada.
