---
id: "44013199049239"
titulo: "[TMS] - Configuração dos correios para preço, prazo e rastreio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013199049239--TMS-Configura%C3%A7%C3%A3o-dos-correios-para-pre%C3%A7o-prazo-e-rastreio"
trilha: "Lincros > TMS > Entregas e Ocorrências - TMS"
atualizado_em: "2026-10-05T19:50:26Z"
rotulos: ["sync_hc", "lincros", "sync_hash_4d98684a9d1e", "lincros_13432860"]
---

# [TMS] - Configuração dos correios para preço, prazo e rastreio

## 1 - Problema Relatado pelo Cliente:

O cliente relatou que precisa configurar a integração com os correios afim de buscar preço, prazo e rastreio dos correios.

## 2 - Passo a Passo para Resolver o Problema:

Com um usuário administrador logado no TMS, acesse: Cadastros Gerais > Transportadoras > Correios > Configurações.

Informe o "Código de Empresa" e a "Senha" utilizados na integração com o serviço **Cálculo de Preço e Prazo**.

Informe o "Usuário" e a "Senha" utilizados na integração com o serviço**Integração de Ocorrências**.

Marque a opção "Integrar com os Correios" para ativar a integração com esses serviços.

![Imagem 1: Marque a opção "Integrar com os Correios" para ativar a integração com esses serviços.](https://ajuda.sankhya.com.br/hc/article_attachments/44013187202455)

## Token

A cada 24 horas é gerado um token o qual é utilizado nas APIs. Para ativá-lo, deve-se preencher os campos da seção API Preço/Prazo/Rastreio: usuário, senha, número cartão são obrigatórios para a ativação, pode-se preencher também **Número Contrato**e**Número DR Contrato.**

![Imagem 2: A cada 24 horas é gerado um token o qual é utilizado nas APIs. Para ativá-lo, deve-se preencher os campos da seção API…](https://ajuda.sankhya.com.br/hc/article_attachments/44013187308951)

Após preencher e salvar, clicar em **Ativar novo WS Correios**. Isto fará a busca do token, o mesmo será populado no campo token, bem como a data de emissão e quando o mesmo irá expirar.

![Imagem 3: Após preencher e salvar, clicar em Ativar novo WS Correios . Isto fará a busca do token, o mesmo será populado no campo…](https://ajuda.sankhya.com.br/hc/article_attachments/44013207730839)

Após realizar todas essas configurações em seu ambiente, abra um ticket com o time de suporte solicitando a habilitação dos seguintes parâmetros para garantir uma melhor performance na utilização dos serviços dos Correios:

**buscarPrazoEntregaCorreios:**Configuração de empresa, que determinar se o prazo de entrega da transportadora correios será buscado via webservice ou será buscado o cadastrado no sistema (fica a sua escolha)

**utilizaNovaApiCorreios:**Quando setado como true, indica que a empresa utiliza a nota API REST do Correios.

Dessa forma, o suporte poderá concluir a configuração e assegurar o correto funcionamento da integração.
