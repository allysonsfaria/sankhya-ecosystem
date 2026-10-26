---
id: "35830167578263"
titulo: "Saiba Mais - Migração das Prefeituras para o Emissor Nacional"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35830167578263-Saiba-Mais-Migra%C3%A7%C3%A3o-das-Prefeituras-para-o-Emissor-Nacional"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > NFS-e"
atualizado_em: "2026-09-15T17:55:38Z"
rotulos: ["Configuração", "Fiscal", "Atualização", "Prefeituras", "NFS-e", "Documentos Eletrônicos"]
---

# Saiba Mais - Migração das Prefeituras para o Emissor Nacional

A Proximidade da Reforma Tributária e a obrigatoriedade da Nota Fiscal de Serviços eletrônica (NFS-e) no Padrão Nacional em diversos municípios, exige proatividade por parte das empresas.

Para que você, nosso cliente em que esteja em um município já obrigatório ao Emissor Nacional (Portal), esteja em total conformidade e evite interrupções na emissão de suas Notas Fiscais, preparamos este guia simplificado de adequação ao **Padrão Nacional da NFS-e**.

**Fique Atento!** Você pode receber um pop-up de aviso em nosso sistema com um link para este **"Saiba Mais"**, confirmando a iminente obrigatoriedade em seu município.

### AVISO IMPORTANTE: Adequação à NFS-e Padrão Nacional

Prezado cliente, para adequar-se às novas regras de consulta e emissão de NFS-e de sua Prefeitura, é necessário essencialmente estar nas seguintes versões do nosso sistema ou superior:

- **4.33b198**
- **4.34b289**
- **4.35b350**

Estando devidamente na versão mínima, siga o passo a passo de configuração abaixo:

### Configuração da NFS-e Padrão Nacional

1. **Valide a Obrigatoriedade e Data de Vigência em Seu Município**

O primeiro e mais importante passo é **validar a obrigatoriedade e a data de vigência** do Padrão Nacional para o perfil da sua empresa (Regime de tributação e porte) diretamente com o seu município (Porto Alegre, Recife ou Belo Horizonte) ou por meio de seu contador.

- **Lembrando:** **NÃO** realize as configurações do Padrão Nacional se a data de vigência da obrigatoriedade ainda não tiver chegado, pois o sistema atual da prefeitura exige configurações específicas, e a ativação antecipada pode gerar erros na emissão.

1. **Ativação da Emissão no Padrão Nacional (Quando na Data de Vigência)**

Se estiver contido na obrigatoriedade do Padrão Nacional e na data de vigência definida pelo seu município, siga o caminho no sistema:

Preferências > [**Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)**>**[Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)**>**[**NFS-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Geral)

Nesta tela, ative a opção **"Emitir NFS-e Padrão Nacional".**

Configure o campo **"Prefixo Série NFS-e Padrão Nacional”** preenchendo com 2 dígitos respeitando o intervalo de 00 a 49.

3. **Configuração da Série e Numeração**

Preencha a **Configuração da Série**, que são campos obrigatórios para o Padrão Nacional com valor numérico entre 1 a 999, bem como a **Numeração**. Recomendamos a numeração automática como uma boa prática.

Para mais informações acesse o artigo: [Como emitir NFS-e no padrão nacional (configuração, tela Empresa)](https://ajuda.sankhya.com.br/hc/pt-br/articles/35604156097559-Como-emitir-NFS-e-no-padr%C3%A3o-nacional-configura%C3%A7%C3%A3o-tela-Empresa).

4. **Atualização do Código de Serviço Municipal**

Na tela de cadastro de [Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos), bem como na aba [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss) e na [Configuração por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaconfiguraesporempresa) e é essencial ressaltar que o **3** precisa ser atualizado para o seguinte formato:

- **Formato Esperado (Exemplo):** Para o serviço que na lista municipal era 01.02, o novo código esperado é **01.02.01**.001
- **Regra Geral:** Para o Portal Nacional, espera-se que o campo seja preenchido com o **item da lista de serviço acrescido do dígito "01" no final** e em alguns municípios espera-se também 001 como código complementar. Consulte a tributação de seu município para ter mais detalhes sobre a informação esperada.

Realizado esses ajustes, sua empresa já estará apta para a emissão da NFS-e pelo Portal Nacional, conforme as regras estabelecidas pelo seu município.

5. **Inclusão do Código NBS**

O preenchimento do **código NBS se tornou obrigatório** em ambiente de homologação e estenderá possivelmente a obrigatoriedade ao ambiente de produção em breve. Siga os passos abaixo para configurá-lo:

- **Habilitar o envio:** Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), acesse a aba [**NFSe**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abanfs-e) e selecione a opção:
  - `Enviar o Código NBS no JSON`

![Imagem 1: Enviar o Código NBS no JSON](https://ajuda.sankhya.com.br/hc/article_attachments/37139852410903)

1. **Vincular ao serviço:** Na tela de cadastro de [Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o), aba [**Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos), preencha o campo:
   - `Código NBS` (correspondente ao serviço prestado).

![Imagem 2: Código NBS (correspondente ao serviço prestado).](https://ajuda.sankhya.com.br/hc/article_attachments/37139852411031)
> **Nota:** Consulte a documentação do município para garantir a conformidade desta informação.

6. **Aprovação da Nota**

A partir de agora, o processo de aprovação das Notas Fiscais de Serviço (NFS-e) será realizado de forma assíncrona. Isso significa que a autorização não será imediata, mas o sistema pode ser configurado para buscar a aprovação automaticamente. Para isso, defina o parâmetro **INTBUSCAAUTNFSE - Intervalo em minutos p/ buscar autorização de NFS-e** com o valor ideal de 1 minuto.

**IBS e CBS nas Notas de Serviços**

- Os impostos já estão estruturados no Sankhya, porém a obrigatoriedade do envio das informações se inicia em 01/01/2026.
- O ambiente de testes do Portal Nacional com as novas informações ainda não está liberado.

Para mais informações acesse o documento: [Documentação antecipada - Migração de Prefeituras](https://docs.google.com/document/d/1PmRa-fY8C1-nZhvm0NMnYKdpo9GK5ZCGaKJg1gASpSU/edit?tab=t.qk9kd9dxpvmb#heading=h.2idvi5jyfei8)
