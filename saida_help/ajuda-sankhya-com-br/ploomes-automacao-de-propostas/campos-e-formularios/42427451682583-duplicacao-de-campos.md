---
id: "42427451682583"
titulo: "Duplicação de campos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427451682583-Duplica%C3%A7%C3%A3o-de-campos"
trilha: "PLOOMES: Automação de propostas  > Campos e formulários"
atualizado_em: "2026-08-10T18:01:55Z"
rotulos: ["sync_hc", "ploomes", "ploomes_15031615", "sync_hash_b482dff112c1"]
---

# Duplicação de campos

## Sobre a duplicação de campos

A duplicação de campos permite criar uma cópia idêntica de um campo já existente, mantendo todas as suas configurações. O recurso ajuda a agilizar a criação de campos similares e evita o retrabalho de configurar tudo manualmente.

## Pré-requisitos

Sem pré-requisitos.

## Utilizando a duplicação de campos

### Duplicando um campo

1. Acesse o campo que deseja duplicar e abra o modal de edição.
2. Clique no ícone de duplicação, localizado à direita do ícone de lixeira.

   ![Imagem 1: Clique no ícone de duplicação, localizado à direita do ícone de lixeira.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2365187487/ebaf2af348c51d6e580914f172e6/image.png?expires=1786536000&signature=d73fd2a92efec1777bf8cea576430d9e0c87835a2e0793369767a89476f1ef3d&req=diMhE8h2moVXXvMW3nq%2BgeoxA9EGDHsQpmoKmvGH7htG83mh6g4g5%2Fh0Azno%0AcvQNnhvD2FwXwXrR1IuLGbu6dA8%3D%0A)
3. Confirme a ação no modal "Você tem certeza que deseja duplicar o campo [Nome do Campo]?".
4. Você será redirecionado para a tela de edição do novo campo, já preenchido com as configurações do original e com o nome **"[Nome do Campo Original] (duplicado)"**.
5. Ajuste o que precisar e salve para concluir a criação.

[GIF animado: Imagem 2: Ajuste o que precisar e salve para concluir a criação.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2365193782/e0808f4ab9f5a972407ceaf72b71/duplicar+campo.gif?expires=1786536000&signature=2338b8f989fe2b21bcd3d19213839b223ecfcd88a6d5ce77651511386ac02ffb&req=diMhE8h3noZXW%2FMW3nq%2BgXcByPOKJ665KfU3MwKxRGVuCqJ17q7TUJm%2BwQze%0Ac09lLqrDXuyinuA%2B3lMH9dV2kBY%3D%0A)

### O que é copiado

Todas as configurações do campo original são replicadas, incluindo tipo do campo, entidade, regras de obrigatoriedade, edição e bloqueio, visualização, integrações externas, valor padrão, texto informativo, campo chave e duas colunas.

A funcionalidade está disponível em qualquer lugar do sistema onde exista edição de campos.

### Limitações da duplicação de campos

- Campos nativos do Ploomes não podem ser duplicados.
- Não é possível duplicar campos entre entidades diferentes.
- Não é possível alterar o caminho (Field Path) do campo duplicado.
- A duplicação é feita individualmente, um campo por vez.
- O ícone de duplicação só aparece em campos já salvos.

## F.A.Q.

1. **Por que não vejo o ícone de duplicação?**

   1. O ícone não aparece em campos nativos do Ploomes nem em campos que ainda não foram salvos pela primeira vez.
2. **Posso duplicar um campo nativo?**

   1. Não. A duplicação está disponível apenas para campos dinâmicos.
3. **Posso mudar a entidade do campo na duplicação?**

   1. Não. O novo campo é sempre criado na mesma entidade do original.
4. **Cliquei em duplicar por engano. Como cancelar?**

   1. Antes de confirmar, clique em **Cancelar** no modal. Se já estiver na tela do novo campo, basta sair sem salvar — o campo só é criado de fato após o primeiro salvamento.

## Glossário

- **Campo dinâmico:** campo personalizado, criado para atender a necessidades específicas do negócio.
- **Campo nativo:** campo estrutural do Ploomes, presente por padrão no sistema.
- **Entidade:** estrutura à qual um campo pertence (ex: Cliente, Negócio, Proposta).
- **Field Path (caminho do campo):** estrutura hierárquica que indica em qual nível o campo está posicionado.
