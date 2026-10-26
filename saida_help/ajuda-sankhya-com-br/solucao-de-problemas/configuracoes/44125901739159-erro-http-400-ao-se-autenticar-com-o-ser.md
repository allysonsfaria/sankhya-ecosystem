---
id: "44125901739159"
titulo: "Erro HTTP 400 ao se autenticar com o serviço externo em integrações"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44125901739159-Erro-HTTP-400-ao-se-autenticar-com-o-servi%C3%A7o-externo-em-integra%C3%A7%C3%B5es"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-09T19:53:21Z"
---

# Erro HTTP 400 ao se autenticar com o serviço externo em integrações

**MENSAGEM**

```
"error":"HTTP 400 Erro ao se autenticar com o serviço externo."
```

**SITUAÇÃO**

Ao executar uma integração, a chamada falha na etapa de autenticação e retorna o erro HTTP 400, impedindo a comunicação com o serviço externo.

A falha ocorre em bases que utilizam a camada de autorização, habilitada pelo argumento

**-Dsnk.authorization.api.enable=true**, quando o usuário vinculado à integração está cadastrado com o tipo incorreto.

**SOLUÇÃO**

O ajuste é feito no cadastro do usuário utilizado pela integração, alterando o tipo de usuário. Não é necessário reiniciar o sistema.

**(1)**  Confirme com a equipe de infraestrutura se o argumento **-Dsnk.authorization.api.enable=true** está ativo no ambiente. Se não estiver, a causa é outra e este artigo não se aplica.

**(2)**  Acesse a tela **Configurações Gateway**, localize a integração que apresentou o erro e verifique o **CODUSU** vinculado a ela.

**(3)**  Acesse a tela **Cadastro de Usuários** e localize o usuário correspondente a esse CODUSU.

**(4)**  Na aba de identificação, localize o campo **Tipo do Usuário**. Se estiver preenchido como **Interface**, altere para **Integração** e salve o registro.

| Tipo do Usuário | Uso |
| --- | --- |
| Interface | Usuários que acessam o sistema pelas telas |
| **Integração** | Usuários utilizados por integrações e serviços. É o tipo correto neste caso |

| **Atenção**  Altere o tipo somente do usuário utilizado pela integração. Usuários que acessam o sistema pelas telas devem permanecer como **Interface**. |
| --- |

Caso o campo não esteja disponível na tela, acesse a engrenagem de configuração e adicione o campo a tela.

**(5)**  Execute novamente a integração e confirme que a autenticação foi concluída e o erro não se repete.

**CAUSA**

Com a camada de autorização habilitada, a autenticação das integrações passa a ser validada por um serviço externo, que verifica o tipo do usuário informado na chamada.

Usuários cadastrados como **Interface** são reconhecidos como usuários de tela e não são aceitos nessa validação. Por isso a autenticação é recusada e a chamada retorna HTTP 400.

Ao alterar o cadastro para o tipo **Integração**, o usuário passa a ser reconhecido como usuário de serviço e a autenticação é concluída normalmente.
