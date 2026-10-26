---
id: "44010075510423"
titulo: "[TMS] - Tabela de frete não localizada: transportadora com mais de um cadastro (CNPJ matriz e filial)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010075510423--TMS-Tabela-de-frete-n%C3%A3o-localizada-transportadora-com-mais-de-um-cadastro-CNPJ-matriz-e-filial"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:29:18Z"
rotulos: ["sync_hc", "lincros", "lincros_17312280", "sync_hash_68e94c895fcd"]
---

# [TMS] - Tabela de frete não localizada: transportadora com mais de um cadastro (CNPJ matriz e filial)

**Menu**: Cadastros Gerais > Transportadoras > Transportadora

**Objetivo**: Identificar quando a tabela de frete não é localizada porque a mesma transportadora possui dois cadastros separados no TMS, e saber como corrigir.

## Sintoma

- Algumas notas ou conhecimentos de uma transportadora calculam o frete normalmente. Outros, da mesma transportadora, não localizam a tabela de frete.
- Nenhuma mensagem de erro é apresentada. O sistema apenas não encontra a tabela.
- Normalmente, os documentos com problema saem com um CNPJ diferente do habitual. Por exemplo, o CNPJ da matriz (/0001) em vez de uma filial (/0003).

## Por que acontece

O TMS localiza a tabela de frete pelo cadastro da transportadora associado ao CNPJ do documento. Se esse CNPJ estiver em um cadastro separado, e não como filial do cadastro que possui a tabela, o sistema não encontra a tabela.

## Como confirmar

1. Acesse Cadastros Gerais > Transportadoras > Transportadora.
2. Filtre a coluna **Nome** pelo nome da transportadora.
3. Se aparecerem duas ou mais linhas da mesma empresa, com a mesma raiz de CNPJ e quantidades de filiais diferentes, a transportadora está duplicada.
4. Verifique em qual dos cadastros a tabela de frete está vinculada. Esse é o cadastro que deve ser mantido.

## Como resolver

A correção é a **unificação de transportadoras**. O cadastro duplicado é absorvido pelo cadastro principal e passa a ser filial dele. Conhecimentos, notas, veículos, motoristas e tabelas são transferidos, e o cadastro duplicado é inativado.

Essa rotina é realizada pela equipe Lincros. Abra um chamado com o suporte informando:

- O CNPJ do cadastro que deve **permanecer** (o que possui a tabela de frete).
- O CNPJ do cadastro que deve ser **unificado** (o duplicado).
- Um print da tela de transportadoras mostrando os dois cadastros.

## Considerações

- A unificação é agendada e executada **fora do horário comercial**, para não impactar documentos em aberto. Valide o resultado no dia útil seguinte.
- Após a unificação, a filial absorvida passa a seguir as configurações do cadastro principal, como modal e **EDI padrão**. Se os dois cadastros utilizavam EDIs diferentes (por exemplo, com ou sem CONEMB), informe o suporte no chamado.
- A partir da versão 4.168.6, a unificação também é concluída quando os dois cadastros estão vinculados à mesma empresa e possuem autorizações de portal em comum.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
