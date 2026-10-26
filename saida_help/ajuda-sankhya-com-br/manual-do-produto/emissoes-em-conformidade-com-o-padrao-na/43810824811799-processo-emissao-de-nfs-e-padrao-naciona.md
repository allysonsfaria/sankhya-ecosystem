---
id: "43810824811799"
titulo: "Processo Emissão de NFS-e Padrão Nacional para tomadores no exterior"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799-Processo-Emiss%C3%A3o-de-NFS-e-Padr%C3%A3o-Nacional-para-tomadores-no-exterior"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Emissões em conformidade com o Padrão Nacional"
atualizado_em: "2026-09-28T11:10:41Z"
---

# Processo Emissão de NFS-e Padrão Nacional para tomadores no exterior

**Caminho de acesso:** Menu Principal › Comercial › Vendas › Central de Vendas › Rodapé › Aba Comércio Exterior

**Versão mínima:** 4.36

**Telas associadas:** [Cadastro de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) · [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros) · [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) · [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799-Processo-Emiss%C3%A3o-de-NFS-e-Padr%C3%A3o-Nacional-para-tomadores-no-exterior) · [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799-Processo-Emiss%C3%A3o-de-NFS-e-Padr%C3%A3o-Nacional-para-tomadores-no-exterior#oque)
- [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799-Processo-Emiss%C3%A3o-de-NFS-e-Padr%C3%A3o-Nacional-para-tomadores-no-exterior#antes)
- [Jornada de uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799-Processo-Emiss%C3%A3o-de-NFS-e-Padr%C3%A3o-Nacional-para-tomadores-no-exterior#jornada)
- [Exemplo de uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799-Processo-Emiss%C3%A3o-de-NFS-e-Padr%C3%A3o-Nacional-para-tomadores-no-exterior#exemplo)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799-Processo-Emiss%C3%A3o-de-NFS-e-Padr%C3%A3o-Nacional-para-tomadores-no-exterior#atencao)
- [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799-Processo-Emiss%C3%A3o-de-NFS-e-Padr%C3%A3o-Nacional-para-tomadores-no-exterior#faq)

## O que é e para que serve

O **Processo Emissão de NFS-e Padrão Nacional para tomadores no exterior** reúne as configurações que o Sankhya Om precisa para emitir a Nota Fiscal de Serviços Eletrônica (NFS-e) no padrão nacional quando o tomador do serviço está no exterior. Nesse cenário, o layout nacional exige um grupo de informações específico de comércio exterior, e o sistema passa a montá-lo automaticamente a partir dos dados parametrizados no Serviço, no Parceiro, na Empresa, no Contrato e na própria nota.

O processo não se aplica a tomadores nacionais: para eles, o grupo de Comércio Exterior não é gerado e a emissão segue sem alteração. Ele também não preenche automaticamente os dados de movimentação temporária de bens, de Declaração de Importação (DI) e de Registro de Exportação (RE) — esses dados são informados manualmente na nota.

---

## Antes de começar

- Confirme com a prefeitura e com o Portal Nacional a disponibilidade do ambiente antes da primeira emissão.
- Configure a emissão de NFS-e no padrão nacional para a empresa. Para saber mais, acesse [Especificações sobre a emissão de NFS-e no padrão nacional](https://ajuda.sankhya.com.br/hc/pt-br/articles/36292338574743-Especifica%C3%A7%C3%B5es-sobre-a-emiss%C3%A3o-de-NFS-e-no-padr%C3%A3o-nacional).

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799-Processo-Emiss%C3%A3o-de-NFS-e-Padr%C3%A3o-Nacional-para-tomadores-no-exterior#sumario)

---

## Jornada de uso

1. Classifique o tomador como estrangeiro. O grupo de Comércio Exterior só é gerado quando o Parceiro (tomador) é estrangeiro, ou seja, quando está vinculado a uma cidade do exterior (UF `EX`) ou possui o campo **ID Estrangeiro** preenchido no [**Cadastro de Parceiros**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros). Para tomadores nacionais, o grupo não é enviado e a emissão segue sem alteração.
2. Parametrize os cadastros base. Informe os padrões de comércio exterior nas telas a que eles pertencem:
   - [**Cadastro de Serviço**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o), aba [**Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos): **Modalidade de Prestação** e **Apoio/Fomento do Prestador**
   - [**Cadastro de Parceiros**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), aba **Fiscal**: **Vínculo Prestador** e **Apoio/Fomento do Tomador**
   - [**Preferências da Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [**Documentos Fiscais Eletrônicos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [**NFS-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e): **Envia para MDIC** (Ministério do Desenvolvimento, Indústria, Comércio e Serviços)
3. Configure as exceções por contrato, se houver. Em [**Contratos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799-Processo-Emiss%C3%A3o-de-NFS-e-Padr%C3%A3o-Nacional-para-tomadores-no-exterior) , aba **Impostos**, tópico **Comércio Exterior**, informe **Modalidade de Prestação** e **Apoio/Fomento do Prestador** quando o acordo com o cliente exigir valores diferentes dos cadastros base. Use o Contrato para tratar exceções de clientes específicos, sem alterar os cadastros base.
4. Informe a moeda estrangeira na nota. No cabeçalho da nota, use o pop-up **Cotação de moedas** para informar a moeda e o valor do serviço na moeda estrangeira. Os dois campos são gravados em conjunto.
5. Complete os dados que não têm herança. Na [**Central de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), no rodapé da nota, acesse a aba **Comércio Exterior** e informe **Mov. Temporária Bens**, **Nº Declaração Importação** e **Nº Registro Exportação** quando aplicável. Esses campos não são herdados de nenhum cadastro.
6. Emita a NFS-e. Ao confirmar a nota, o sistema monta o grupo de Comércio Exterior no arquivo de envio, com os valores resolvidos pela regra de precedência.

**💡 Dica**

Parametrize primeiro o Serviço, o Parceiro e a Empresa: assim o faturista não precisa preencher a aba **Comércio Exterior** nota a nota.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799-Processo-Emiss%C3%A3o-de-NFS-e-Padr%C3%A3o-Nacional-para-tomadores-no-exterior#sumario)

---

## Exemplo de uso

Uma empresa presta serviço de desenvolvimento de software para um cliente nos Estados Unidos. O Serviço está com **Modalidade de Prestação** igual a **Transfronteiriço**, o Parceiro com **Vínculo Prestador** igual a **Sem vínculo** e a Empresa com **Envia para MDIC** igual a **Não enviar**. O faturista informa a moeda USD pelo pop-up **Cotação de moedas** e emite a nota: o grupo de Comércio Exterior é montado automaticamente.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799-Processo-Emiss%C3%A3o-de-NFS-e-Padr%C3%A3o-Nacional-para-tomadores-no-exterior#sumario)

---

## Pontos de atenção

- O preenchimento automático obedece à ordem Nota › Contrato › Cadastros base. O valor digitado na nota prevalece e não é sobrescrito pelo sistema.
- Os campos **Mov. Temporária Bens**, **Nº Declaração Importação** e **Nº Registro Exportação** não possuem herança e devem ser informados manualmente na nota.
- Os novos campos são apresentados vazios por padrão. Quando não preenchidos nem herdados, o sistema envia os valores padrão descritos em [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799-Processo-Emiss%C3%A3o-de-NFS-e-Padr%C3%A3o-Nacional-para-tomadores-no-exterior#faq).
- Sem moeda estrangeira informada na nota, o envio considera Real (BRL).
- Para tomadores nacionais, o grupo de Comércio Exterior não é gerado, em nenhuma das formas de emissão.

**⚠️ Atenção**

Com o campo **Mov. Temporária Bens** igual a **Vinculada RE**, informe o **Nº Registro Exportação**. Emitir para tomador estrangeiro sem esse número resulta em rejeição do documento.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799-Processo-Emiss%C3%A3o-de-NFS-e-Padr%C3%A3o-Nacional-para-tomadores-no-exterior#sumario)

---

## Perguntas frequentes

### Quando o grupo de Comércio Exterior é enviado?

Somente quando o tomador é estrangeiro, ou seja, vinculado a uma cidade do exterior (UF `EX`) ou com o campo **ID Estrangeiro** preenchido.

### Preciso preencher a aba Comércio Exterior em toda nota?

Não. Se os cadastros de Serviço, Parceiro, Empresa ou o Contrato estiverem parametrizados, o sistema preenche automaticamente. A aba serve para conferência e para exceções.

### O que o sistema envia quando um campo não é preenchido nem herdado?

- **Vínculo Prestador**: **Sem vínculo com o tomador**
- **Moeda**: BRL
- **Apoio/Fomento do Prestador** e **Apoio/Fomento do Tomador**: **01 - Nenhum**
- **Mov. Temporária Bens**: **Não**
- **Envia para MDIC**: **Não**

### Alterei o valor na nota. O sistema sobrescreve?

Não. O valor informado manualmente na nota tem prioridade máxima e é preservado.

### Como a moeda é enviada?

O sistema converte a sigla da moeda informada na nota no código numérico correspondente da tabela do Banco Central. Sem moeda estrangeira, usa o Real.
