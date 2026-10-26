---
id: "39383668743191"
titulo: "Erro ao aplicar filtro - Subconsulta Retornou Mais de Um Valo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39383668743191-Erro-ao-aplicar-filtro-Subconsulta-Retornou-Mais-de-Um-Valo"
trilha: "Solução de Problemas > Erros Internos"
atualizado_em: "2026-08-27T02:31:03Z"
rotulos: ["SQL", "Configuração", "Portal de Vendas", "Estoque", "Erro", "Artigo criado KCS", "Plataforma - KCS"]
---

# Erro ao aplicar filtro - Subconsulta Retornou Mais de Um Valo

**Mensagem**

A subconsulta retornou mais de 1 valor. Isso não é permitido quando a subconsulta segue =, !=, <, <=, >, >= ou quando ela é usada como uma expressão.

**Situação**

Ao tentar aplicar filtros (como filtros de data ou outros critérios) em telas como o Portal de Vendas, o sistema apresenta este erro de subconsulta, bloqueando a tela e impedindo a visualização dos dados filtrados.

**Solução**

**(1)** **Identifique os campos suspeitos:** Verifique os "Campos Adicionais" da tabela afetada (ex: `TGFCAB`) que possuem expressões SQL configuradas.

**(2)** **Acesse o Monitor de Consultas:** Vá em `Configurações > Avançado > Monitor de Consultas` e capture a consulta exata que está travando o sistema.

**(3)** **Isole o problema no DBE:** Execute a consulta capturada no DBExplorer. Para descobrir qual campo é o culpado, transforme temporariamente a expressão dos campos suspeitos em comentários.

Exemplo de como comentar um trecho do script:

```
/* (
SELECT SUM(EST.ESTOQUE)
FROM TGFEST EST
WHERE EST.CODPROD = TGFPRO.CODPROD
 AND EST.CODEMP = 9
) AS AD_EXEMPLO, */
```

**(4)** **Trate o campo problemático:** O campo que, ao ser comentado, fizer a consulta rodar com sucesso é a origem do erro. Atenção: Não remova a expressão imediatamente, pois isso pode impactar processos do cliente. Oriente-o a acionar o responsável pela criação do campo para ajustar a regra SQL, garantindo que o retorno seja estritamente de um valor por registro. A remoção temporária ou definitiva da expressão só deve ser feita mediante autorização prévia do cliente.

**(5)** **Valide a solução:** Realize um teste funcional na tela original (ex: Portal de Vendas), preferencialmente em horários de menor fluxo operacional, para confirmar a correção.

**Causa**

O erro no banco de dados ocorre porque há Campos Adicionais (ex: `AD_XXXXX`) ou Ligações na tabela de origem (como a `TGFCAB`) configurados com expressões SQL que estão retornando múltiplos registros, quando o sistema espera apenas um único valor.
