---
id: "42427443766039"
titulo: "Como preencher automaticamente o primeiro nome do cliente?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427443766039-Como-preencher-automaticamente-o-primeiro-nome-do-cliente"
trilha: "PLOOMES: Automação de propostas  > Clientes"
atualizado_em: "2026-08-10T18:03:33Z"
rotulos: ["sync_hc", "ploomes", "ploomes_6773143", "sync_hash_b0724de5980e"]
---

# Como preencher automaticamente o primeiro nome do cliente?

No Ploomes, é possível criar um campo personalizado com fórmula para armazenar automaticamente apenas o primeiro nome do cliente, tornando seus processos mais eficientes conforme a necessidade.

Além disso, é possível configurar uma automação para preencher esse campo nos clientes que já estão cadastrados na conta.

## Como criar o campo?

- Acesse **Administração > Campos e formulários**;
- Clique em **Cliente** e, em seguida, selecione o formulário que deseja editar (**Empresas** ou **Pessoas**);
- Selecione **Adicionar campo > Criar campo;**
- Escolha o tipo **Texto simples** e defina um **Título** para o campo, por exemplo: Primeiro Nome;
- Clique em **Configurações avançadas > Configurar.**

Utilize a seguinte fórmula:

```
("[Cliente.Nome]").split(' ').slice(0, 1).join(' ');
```

**⚠️ Importante:** O campo deve ser inserido manualmente por meio do botão **Campos**, para que seja adicionado corretamente como variável na fórmula.

[GIF animado: formula dentro do campo](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2049890838/94c94cf60c55456d74d76d707e05/formulaNome.gif?expires=1786536000&signature=385092f0d45b062247087a17f74fb91c700e5297f1e4e4949d39b26d2fb768af&req=diAjH8F3nYlcUfMW3nq%2BgR1Aq3pEqri7kAU5BS5WQcEYtlfxXzOfjBo%2FwZcA%0Aej2MTkek0hFYE6ITpxHPOzWdqSs%3D%0A)

Após concluir a configuração, salve a fórmula, depois salve o campo e, por fim, salve o formulário para aplicar as alterações.

## Como fazer a automação?

**⚠️ Importante:** para realizar esse passo, é necessário ter contratado o **Módulo de Automações**. Caso ainda não tenha, entre em contato com o **Suporte** ou com a sua **Gerente de Contas** para obter mais informações.

- Acesse **Administração** > **Automações**;
- Selecione **Cliente** > **Nova automação**;
- Defina o titulo da automação, como por exemplo: "Preenche Primeiro Nome";
- No campo **Gatilho**, selecione **Periodicamente**. A **Execução** pode ser configurada com qualquer intervalo, pois a automação será executada apenas uma vez e, em seguida, desabilitada;
- (Opcional) No **Filtro**, configure: **Cliente > Tipo > Igual a > Pessoa**, para que o campo seja preenchido apenas para clientes do tipo Pessoa;

  ![automação](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2049843327/15e503718d5525678ba34662fc02/image.png?expires=1786536000&signature=5943f3ef851b4a2c3243afa408304d67c1c4455230ca525cacdf55695905eb81&req=diAjH8F6noJdXvMW3nq%2BgUTqG5EUxs7Vp077J7Y67Fpp4OfqK6S1NWplbZMr%0AsEm5bBoo5kYFkiTzp1RNl4WqzIA%3D%0A)
- Configure a automação para **Editar dados** > **Cliente** > **Primeiro Nome** > **Fórmula;**

Utilize a seguinte fórmula:

```
("[Cliente.Nome]").split(' ').slice(0, 1).join(' ');
```

**⚠️ Importante:** O campo deve ser inserido manualmente por meio do botão **Campos**, para que seja adicionado corretamente como variável na fórmula.

[GIF animado: Editar dados](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2049849695/1a44b35f191684c92de58fd30e8e/automacaoNome.gif?expires=1786536000&signature=649772acc4bce25e5cf3c99b25e85ec197706d74efd1e0331aee7dd65de3b525&req=diAjH8F6lIdWXPMW3nq%2BgZGtje3fyJgj%2FVQdiw%2FYffxz5tGjNrBSyXFArTDe%0AhmiGJqeq9vrUJksUY8%2BB8%2FVTRRA%3D%0A)

Após configurar a ação, salve a fórmula e clique em **Salvar**.

Em seguida, acesse a automação criada e selecione **Salvar e executar agora** para que ela seja executada e preencha o campo nos clientes já cadastrados na conta.

![salvar e executar](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2049858814/2d4a80fe2bf3a4aa3a6564126a21/image.png?expires=1786536000&signature=2afabb5b066b81dde3336d90409688aafdeadbfee46004b6030a0588d742bf12&req=diAjH8F7lYleXfMW3nq%2BgV7FSQZPlt%2Fj8VgNI1ER1ETV%2F3DUC7TOdmXMV8dq%0AHx16iSBp%2BEusqbt82M9xEKVyqsY%3D%0A)

Após a execução, a automação pode ser excluída ou desabilitada para evitar que seja executada novamente sem necessidade.

![desabilitar](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2049864379/334b530605d26cb964f0b09a6286/image.png?expires=1786536000&signature=8edaaf324d90980763aceea2ff4bc18e7ed86a5edda6cdf46351e9c244c4bc4c&req=diAjH8F4mYJYUPMW3nq%2BgeTlOSbDOl9Z2wFz26xYR0%2FY3sdMm0zOSA8p9uEz%0Axw0eNzR5rNNn0dS%2F%2F0zj4L2Sf%2Fg%3D%0A)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
