---
id: "44011291058199"
titulo: "[TMS] - Como realizar o De/Para de Componentes de Frete no Cadastro de Transportadoras para a Auditoria de Fretes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011291058199--TMS-Como-realizar-o-De-Para-de-Componentes-de-Frete-no-Cadastro-de-Transportadoras-para-a-Auditoria-de-Fretes"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:00:55Z"
rotulos: ["sync_hc", "lincros", "lincros_13438755", "sync_hash_2354699847ba"]
---

# [TMS] - Como realizar o De/Para de Componentes de Frete no Cadastro de Transportadoras para a Auditoria de Fretes

## 1 - Problema Relatado pelo Cliente

O cliente precisa realizar o cadastro de componentes informados pela transportadora no XML do CT-e, a fim de garantir a correta auditoria das tabelas de frete. A ausência deste cadastro impede a correlação adequada entre os componentes enviados pela transportadora e os componentes padrões do TMS, prejudicando a consistência das informações e análises de auditoria de fretes na aba Movimentos do pré-conhecimento.

---

## 2 - Passo a Passo para Resolver o Problema

## De/Para de Componentes - Tela de Cadastro de Transportadora

1. **Acessar o menu:**

   - Cadastros Gerais > Transportadoras > Transportadora (Empresa)
2. **Selecionar a transportadora:**

   - Escolha a transportadora para a qual deseja realizar o De/Para de Componentes.
   - Na listagem de transportadoras, clique no código de identificação para acessar o cadastro.
3. **Incluir novo De/Para de Componente:**

   - Ao entrar no registro da transportadora, entrando pelo código, ir na aba Componentes
   - Clique no botão "(+) Incluir". Será aberta uma tela com três campos:
4. **Realizar o De/Para:**

   - No campo “Código De/Para do Componente”, insira o nome do componente informado pela transportadora, o mesmo informado no XML do CT-e.
   - No campo “Componente”, selecione o componente correspondente do TMS
   - No campo “Tipo de Rateio”, selecione a forma de rateio da transportadora para este componente. O tipo de Rateio será utilizado para ratear os valores calculados por este componente no Embarque, entre todos os CT-es do embarque. Somente preencha essa informação se para essa transportadora e para esse componente, o sistema deverá realizar um rateio diferente, caso contrário, o sistema continuará a realizar o rateio deste componente de frete no embarque conforme configuração do parâmetro de empresa tipoRateioCarga
   - ![Imagem 1: No campo “Tipo de Rateio”, selecione a forma de rateio da transportadora para este componente. O tipo de Rateio será…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1964948875/9c39835aef7ece0c2faccb7926fa/7E46B398C8F05B7AFA2FB2679A7587E8?expires=1791331200&signature=6355b4c121613c6e7d9084abb40baf50ea14dbd1ba3717b385574888b7179c7b&req=dSkhEsB6lYlYXPMW3nq%2BgX29Z58q3zcAuynuINsEGqBienN3KIbgYniffNeK%0ApPCeXr6fOMRx5Z2VjOOxZZQiHSc%3D%0A)
5. **Salvar as informações:**

   - Clique em **‘Incluir’** para adicionar o novo registro.
   - Em seguida, clique em **‘Salvar’** para confirmar e gravar o De/Para de Componentes.
