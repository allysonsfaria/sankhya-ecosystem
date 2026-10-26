---
id: "42950731345559"
titulo: "Contatos não são exibidos nas Soluções Vidya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950731345559-Contatos-n%C3%A3o-s%C3%A3o-exibidos-nas-Solu%C3%A7%C3%B5es-Vidya"
trilha: "VIDYA: Vendas externas, televendas e entregas > Geral"
atualizado_em: "2026-08-24T13:39:56Z"
rotulos: ["sync_hc", "vidya", "vidya_594699", "sync_hash_bcb7f54d41a3"]
---

# Contatos não são exibidos nas Soluções Vidya

## Sintoma

O cliente informa que os contatos estão cadastrados corretamente no ERP, porém, ao consultar os contatos nas Soluções Vidya, nenhum registro é apresentado.

Apesar de o cadastro existir na base de dados, os contatos não ficam disponíveis para consulta pelos usuários.

---

### Causa

Esse comportamento normalmente ocorre quando o parâmetro **Cadastro de Contatos: Somente leitura** não está habilitado.

Sem essa configuração, as Soluções Vidya podem não considerar os contatos cadastrados para exibição.

---

### Solução

1. Acesse a tela de Configurações Vidya Force.
2. Localize o parâmetro **Cadastro de Contatos**
3. Habilite o parâmetro com a opção **Somente Leitura**.
4. Salve a alteração.

Após a configuração, realize uma nova consulta dos contatos nas Soluções Vidya.

---

### Validação

Após habilitar o parâmetro:

- Verifique se os contatos estão cadastrados corretamente no ERP.
- Acesse as Soluções Vidya.
- Consulte o cadastro do parceiro.
- Confirme se os contatos passam a ser exibidos normalmente.

---

### Quando utilizar este artigo

Utilize esta validação sempre que:

- Os contatos existirem no ERP.
- O cadastro estiver correto.
- As Soluções Vidya não apresentarem os contatos ao usuário.
- Não houver erros aparentes de sincronização.

Antes de iniciar uma análise mais aprofundada, valide esse parâmetro, pois ele pode resolver o problema de forma imediata.
