---
id: "43547139729303"
titulo: "Ausência do cálculo de IBS na NFS-e após configuração de IBS/CBS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43547139729303-Aus%C3%AAncia-do-c%C3%A1lculo-de-IBS-na-NFS-e-ap%C3%B3s-configura%C3%A7%C3%A3o-de-IBS-CBS"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária"
atualizado_em: "2026-10-09T21:22:22Z"
rotulos: ["Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# Ausência do cálculo de IBS na NFS-e após configuração de IBS/CBS

**Mensagem**

A NFS-e é emitida sem apresentar o cálculo do IBS, mesmo após a configuração dos campos de IBS/CBS no sistema. Não há mensagem de erro explícita no momento da emissão.

**Situação**

O usuário realizou a configuração dos campos de IBS/CBS nas telas **"Tipos de Operação - TOP"** (Configurações Cadastros Tipos de Operação), aba **"Impostos"**, e também no cadastro de serviço. Após essas configurações, ao emitir uma Nota Fiscal de Serviço Eletrônica (NFS-e), o valor do IBS/CBS não é calculado nem apresentado no documento, mesmo com as alíquotas e códigos de situação tributária devidamente preenchidos.

**Solução**

Para garantir o correto cálculo do IBS na NFS-e após a configuração dos campos de IBS/CBS, siga o passo a passo abaixo:

**(1)** Verifique se o campo **"Código NBS"** está preenchido corretamente no cadastro do serviço (**Configurações » Cadastros » Serviços**). Ao cadastrar as alíquotas de IBS e CBS, utilize o **NBS** como classificação fiscal do serviço, e não o **NCM**, que é utilizado para produtos. O preenchimento correto do NBS é importante para que o sistema identifique e selecione a alíquota correspondente ao serviço na nota fiscal.

**(2)** Confirme se o campo **"Código Classificação Tributária Nacional"** está preenchido na aba de tributação do serviço. Este campo é essencial para o cálculo do IBS/CBS.

**(3)** No cadastro da TOP utilizada na emissão da NFS-e (**Comercial » Arquivo » Cadastros » Tipos de Operação – TOP**), acesse a aba **"Impostos"** e verifique se os campos **"Tem IBS" e "Tem CBS** estão marcados.

**(4)** Verifique se a configuração da alíquota de IBS/CBS está vigente para a data de emissão da NFS-e. Caso necessário, ajuste a vigência na tela de cadastro de alíquotas.

**(5)** No cadastro do serviço (**Configurações » Cadastros » Serviços**), verifique se o campo **"NCM"** está preenchido. Para serviços, utilize o campo **"NBS"** como classificação fiscal. Caso exista um NCM informado no cadastro do serviço, o sistema poderá deixar de calcular os impostos de IBS e CBS.

Para verificar se existe NCM preenchido no cadastro do serviço, acesse o **DBExplorer** e execute a seguinte consulta:

```
SELECT CODPROD, DESCRPROD, NCM, NBS
FROM TGFPRO
WHERE CODPROD = (insira o número do serviço)
```

**(6)** Após revisar as configurações, salve e emita novamente a NFS-e para validar se o cálculo do IBS foi realizado corretamente.

Caso o problema persista, revise as regras de validação do sistema, pois campos obrigatórios não preenchidos ou inconsistências podem impedir o cálculo automático do IBS, mesmo sem apresentar mensagem de erro.

**Causa**

A ausência do cálculo do IBS na NFS-e, mesmo após a configuração dos campos de IBS/CBS, geralmente ocorre devido a um ou mais dos seguintes fatores:

- O campo **"Código NBS"** não foi preenchido corretamente no cadastro do serviço ou na Aliquota de IBS/CBS.
- As alíquotas de IBS/CBS não estão vigentes para a data da emissão.
- Há conflito entre os campos **"NCM"** e **"NBS"** no cadastro do item/serviço.
- Configurações obrigatórias não foram salvas corretamente, impedindo o cálculo automático pelo sistema.

A correta configuração e preenchimento dos campos fiscais é fundamental para que o sistema realize o cálculo do IBS na emissão da NFS-e.
