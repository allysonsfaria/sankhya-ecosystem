---
id: "42950963717399"
titulo: "token_invalido: link de preenchimento do gestor inválido ou desativado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950963717399-token-invalido-link-de-preenchimento-do-gestor-inv%C3%A1lido-ou-desativado"
trilha: "MITRA: Planejamento orçamentário  > Link do gestor"
atualizado_em: "2026-08-24T13:48:28Z"
rotulos: ["sync_hc", "mitra", "mitra_4", "sync_hash_89f4a3a45dc6"]
---

# token_invalido: link de preenchimento do gestor inválido ou desativado

## token\_invalido: link de preenchimento do gestor inválido ou desativado

### Mensagem

```
{"ok": false, "error": "token_invalido"}
```

Este é o retorno das operações do link de preenchimento quando o token não é reconhecido ou está desativado. [VALIDAR: texto exato exibido na interface para o usuário nesta situação]

Variação conhecida:

```
{"ok": false, "error": "params_invalidos"}
```

Retornada quando a chamada chega sem os dados obrigatórios (por exemplo, URL do link incompleta ou corrompida).

### Situação

O gestor acessa o link de preenchimento recebido por e-mail e a página não carrega seus centros de resultado, ou as ações de salvar e submeter falham. O erro impede qualquer operação pelo link.

### Causa

O acesso pelo link usa um token exclusivo, gerado **por versão do orçamento e por gestor**, com controle de ativação e expiração. As causas confirmadas são:

1. **Versão fechada:** o fechamento de uma versão desativa automaticamente os tokens dos links daquela versão. Links de versões anteriores deixam de funcionar de forma definitiva.
2. **Link desatualizado:** o gestor está usando um e-mail antigo, de uma versão que não é mais a vigente.
3. **URL incompleta:** o endereço foi copiado pela metade ou alterado, e o token chega inválido ou ausente (`params_invalidos`).

### Solução

1. Confirme com o gestor se ele está usando o **e-mail mais recente** com o link de preenchimento.
2. Peça para copiar e colar a URL completa do e-mail no navegador, sem cortes.
3. Se o erro continuar, gere e reenvie um novo link da versão vigente para o gestor. [VALIDAR: rótulo do botão de geração/reenvio de link]
4. Peça ao gestor para acessar o novo link e repetir a operação.

### Resultado esperado

A página inicial do link abre com os cartões dos centros de resultado e pacotes do gestor, com status e progresso de preenchimento, e as ações de salvar e submeter voltam a funcionar.

### Se o problema continuar

Reúna as seguintes evidências antes de encaminhar para suporte:

- URL completa utilizada (sem repassar a terceiros);
- e-mail e nome do gestor;
- nome da versão do orçamento em uso;
- data e hora da tentativa;
- captura de tela do erro exibido.

---

### Pendências para validação

1. `[VALIDAR: texto exato exibido na interface para o usuário nesta situação]` — capturar a mensagem visível na tela do link.
2. `[VALIDAR: rótulo do botão de geração/reenvio de link]` — confirmar o botão de reenvio.
