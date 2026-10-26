---
id: "360044295653"
titulo: "O que é Certificado digital e para que serve?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044295653-O-que-%C3%A9-Certificado-digital-e-para-que-serve"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:58:53Z"
rotulos: ["DUVIDANF", "A1", "A3", "CERTIFICADO DIGITAL", "NFE", "Nota Fiscal Eletronica", "SANNFE", "Configuração", "Segurança", "NF-e", "Certificado Digital: A1 vs. A3", "Documentos Eletrônicos"]
---

# O que é Certificado digital e para que serve?

**(1)** O certificado digital é indispensável para as empresas que emitem Documentos Eletrônicos (NFe, NFSe, NFCe, ECF, MDFe, EFD etc...). Abaixo serão mostradas as características e diferenças do certificado A1 e A3.

#### Imagem 1: O que é certificado digital? O que é certificado digital?

- O certificado digital é um documento eletrônico que é a identidade da pessoa jurídica. Ele contém o nome, um número exclusivo conhecido por chave pública e outros dados que identificam a sua empresa na Receita Federal e nos sistemas de gestão.
- O certificado digital para pessoa jurídica é dividido em dois documentos distintos: o e-CNPJ e o eNF-e. Ambos podem ser utilizados para emissão de NF-e, mas eles têm diferenças.
- O e-CNPJ deve ser usado exclusivamente pelo representante legal da empresa, pois dá acesso a várias informações e a todos os documentos da empresa. Em regra geral, esse certificado é mais barato que o eNF-e.
- Já o eNF-e pode ser usado também pelos funcionários, pois sua função é basicamente a emissão de NF-e. Ele foi criado para atender grandes demandas de emissão de nota fiscal eletrônica e por isso, normalmente, ele é mais caro.
- Com o eNF-e não é possível acessar o CAC e a Conectividade Social.
- A nível de curiosidade: existe também o e-CPF, o certificado digital para pessoa física, mas esse não é o foco deste artigo.

#### Imagem 2: E a segurança, como fica? E a segurança, como fica?

- O certificado digital tem duas chaves, uma pública e outra privada.
- A chave privada é como se fosse uma fórmula matemática que gera um código exclusivo para cada documento que a sua empresa emitir.
- Já a chave pública possibilita a leitura desse código e o reconhecimento que o documento é autêntico.
- Esse código é reconhecido pela SEFAZ, pois ela também tem o conhecimento da sua chave pública.
- Sem o conhecimento da chave não é possível entender esses dados e se o código estiver incorreto, o documento não é válido. Assim, ninguém consegue emitir e assinar algum documento por você, garantindo sigilo e segurança para sua empresa.
- O certificado digital, em regra geral, mantém as seguintes informações: nome, período de validade do certificado digital, chave pública, nome e assinatura da autoridade que assinou o certificado e número de série.
- E então surge mais uma divisão. Ambos os certificados: e-CNPJ e eNF-e têm duas opções: o A1 e o A3. Conheça a seguir a diferença entre eles:

**![Imagem 3: Diferença entre certificado A1 E A3](https://ajuda.sankhya.com.br/hc/article_attachments/17294863952919) Diferença entre certificado A1 E A3**

No caso da Sankhya, é utilizado somente o Certificado A1, com extensão .PFX.

(2)**Certificado A1**

- O certificado A1 é um documento eletrônico que é instalado diretamente no computador e não depende de cartões ou tokens para o seu uso. É um arquivo que normalmente possui extensão .PFX ou .P12.
- A sua senha de acesso precisa ser digitada uma única vez, durante a instalação do certificado, não sendo necessário informá-la nas emissões de NF-e, por exemplo.
- Esse certificado tem muitas vantagens:
  - Por ser apenas um arquivo é livre de desastres naturais, roubos e extravios.
  - Pode ser usado em diversas plataformas: smartphones, tablets e notebooks, isso quer dizer que é possível emitir notas fiscais até do seu celular.
  - Apenas um certificado é necessário para matriz e filiais, sem preocupações em ter que levar e buscar o certificado a cada utilização.
  - A sua validade é de apenas um ano.

(2)** Certificado A3**

- Uma das grandes diferenças do certificado digital do tipo A3 é que ele é armazenado em algum hardware: token ou cartão.
- Esse tipo de certificado só pode ser usado em um único equipamento por vez, pois o cartão ou o token precisa estar conectado no equipamento. Então se quiser utilizar em dois equipamentos de forma simultânea, não é possível.
- Sempre que decidir utilizar em outro equipamento é necessário levar o hardware até ele e fazer uma nova configuração.
- Para utilizá-lo, nesses casos, é preciso que você leve o dispositivo da matriz até a filial para a emissão da NF-e.
- O certificado A3 também possui uma senha de acesso. Mas, essa precisa ser informada diariamente. Caso você digite três vezes a sua senha errada, o certificado será bloqueado e é necessário adquirir um novo certificado. O token e o cartão, nesses casos, podem ser reaproveitados.
- O preço desse certificado é mais acessível se considerarmos o preço por ano. Mas, é necessário adquirir um dispositivo para leitura do certificado que pode sofrer alguma avaria.
- Nesses casos é necessário adquirir um dispositivo novo e o preço do certificado A3 acaba ficando maior do que o A1.
- As suas desvantagens também são maiores:
  - Por ser um dispositivo há vulnerabilidade a furtos, extravios e desastres naturais.
  - Precisa de uma entrada USB para ler tokens e, além disso, uma leitora em caso de cartões.
  - Apenas um computador por vez pode emitir nota, além disso é necessário o deslocamento do token ou cartão para o equipamento que vai emitir esse documento. O que pode ser um transtorno em caso de empresas que mais de uma pessoa emite NF-e ou entre matriz e filial.
  - Não pode ser utilizado em dispositivos móveis, como smartphones e tablets.
  - É preciso ter um certificado para cada filial, pois há o limitador físico do certificado estar conectado na máquina de emissão da NF-e.
  - Precisa digitar a senha no momento da autorização das notas.
  - Caso aconteça alguma alteração no contrato social, é necessário trocar de certificado.

#### Imagem 4: Qual o mais seguro: A1 ou A3? Qual o mais seguro: A1 ou A3?

- Esta é uma dúvida bem recorrente. A resposta mais simples para esta pergunta é: **não faz diferença para a maioria dos casos**. Mas, caso não esteja convencido e queira uma explicação um pouco mais técnica, continue lendo para entender melhor.
- Como dissemos antes, a diferença entre o certificado A1 e o A3 é que o A3 fica armazenado dentro de um dispositivo como um token ou um cartão. Estes dispositivos são como pequenos computadores.
- Já o certificado A1 fica armazenado no seu computador que realizará a assinatura digital do documento.
- Quando você assina um documento com o certificado A1, o seu próprio computador efetuará a assinatura com a ajuda do certificado.
- No caso do A3, o seu computador pede para o token ou o cartão assinar o documento. O trabalho é todo feito pelo dispositivo e seu computador não tem acesso ao certificado armazenado nele.
- Sob o ponto de vista de segurança, para o envio de NF-e ou coisas simples como tal, isso não faz muita diferença.

#### Imagem 5: Todas as empresas são obrigadas a adquirir o certificado digital? Todas as empresas são obrigadas a adquirir o certificado digital?

- Quem precisa emitir NF-e sim, segundo o ajuste SINIEF 12/16.
- As empresas inscritas no Lucro Real e no Lucro Presumido também são obrigadas a ter um certificado digital, já que a maioria das declarações mensais e anuais só podem ser realizadas através do certificado digital, obrigação vinda da Receita Federal.
- Já as do Simples Nacional, precisam adquirir se tiverem mais de cinco funcionários, para prestarem informações trabalhistas, fiscais e previdenciárias pela GFIP e eSocial.
- É importante lembrar que com a aquisição do eNF-e, sua empresa poderá apenas emitir NF-e e precisará adquirir um eCNPJ para enviar essas outras informações.

#### Imagem 6: Como obter um certificado digital? Como obter um certificado digital?

- O primeiro passo é escolher uma Autoridade Certificadora.
- A Autoridade Certificadora é a empresa autorizada pela Receita Federal a autorizar e certificar sua empresa. Você pode ter maiores informações sobre Autoridades Certificadoras no site do Instituto Nacional de Tecnologia da Informação – ITI.
- Assim que entrar em contato com a Autoridade Certificadora, será marcado um horário para entrega dos documentos necessários e então você escolherá qual tipo de certificado deseja.
- Depois é só efetuar o pagamento e pronto!

**(1)** Ainda ficou com alguma dúvida sobre certificado digital? Deixe seu comentário!
