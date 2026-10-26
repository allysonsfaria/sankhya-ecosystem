---
id: "42427323674007"
titulo: "Como funciona o reconhecimento facial no registro pelo app"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427323674007-Como-funciona-o-reconhecimento-facial-no-registro-pelo-app"
trilha: "PONTOTEL: Sistema de marcação de ponto > Registro de Ponto"
atualizado_em: "2026-08-03T13:29:35Z"
rotulos: ["sync_hc", "pontotel", "sync_hash_7466c5af566f", "pontotel_6a3329eb7990d448393c9dec"]
---

# Como funciona o reconhecimento facial no registro pelo app

O **reconhecimento facial** é uma tecnologia de segurança utilizada pela Pontotel para validar a identidade do colaborador no momento do registro de ponto. Essa funcionalidade garante mais confiabilidade ao processo, reduz riscos de fraude e facilita a gestão da jornada.

Este artigo é um complemento ao conteúdo de [como configurar e gerenciar o reconhecimento facial](https://sankhya.zendesk.com/hc/pt-br/articles/42427252165271). Aqui, vamos explicar como o recurso funciona na prática durante o uso pelos colaboradores.

---

## Como ocorre o processo de reconhecimento facial no app BatePonto

1. **Captura da imagem**

   No momento do registro, a câmera do dispositivo é ativada para fazer o recohecimento facial. Esse processo pode ocorrer antes ou depois do preenchimento do PIN. a depender de como está configurado o [perfil de coletor](https://sankhya.zendesk.com/hc/pt-br/articles/42427310963095#3-passo-a-passo-para-gerenciar-perfil-de-coletores).
2. **Comparação com a base de dados**

   O sistema compara a foto tirada com as imagens cadastradas e aprovadas previamente na [Gestão de Biometria Facial](https://sankhya.zendesk.com/hc/pt-br/articles/42427252165271#3-biometria-facial)**.**
3. **Validação da identidade**

   Se a foto corresponder ao padrão cadastrado, as informações do colaborador serão exibidas para confirmação.
   Após confirmar os dados e escolher o tipo de registro (entrada, pausa, saída etc.), o ponto é salvo normalmente.

   [GIF animado: Imagem 1: Se a foto corresponder ao padrão cadastrado, as informações do colaborador serão exibidas para confirmação. Após…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/comprimido_1f92ip6.gif)

   Caso contrário, o sistema poderá bloquear o ponto ou exigir a digitação do PIN (caso o reconhecimento facial seja feito antes), dependendo da configuração definida pela empresa.
   Após a confirmação dos dados, a câmera abrirá novamente, mas dessa vez para registrar uma foto comum junto ao ponto (caso essa funcionalidade esteja habilitada).

   [GIF animado: Imagem 2: Caso contrário, o sistema poderá bloquear o ponto ou exigir a digitação do PIN (caso o reconhecimento facial seja feito…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/comprimido-3_15dgahp.gif)

   Alguns fatores podem comprometer a validação da imagem e gerar falhas:
   \* Câmera suja ou embaçada.
   \* Rosto cortado ou fora de foco.
   \* Ambiente escuro ou com luz diretamente contra o rosto.
   \* Foto feita em ângulo incorreto (de lado, de cima ou de baixo).
   \* Uso de acessórios que dificultem a identificação, como filtros, óculos escuros, bonés ou máscaras.
   \* Presença de outras pessoas na foto ou no fundo da imagem

---

## Observações

- Para que o reconhecimento facial funcione corretamente, o colaborador precisa ter **fotos de qualidade cadastradas** na [Gestão de Biometrias](https://sankhya.zendesk.com/hc/pt-br/articles/42427252165271#3-biometria-facial).
- A funcionalidade depende da câmera do dispositivo estar funcionando e com permissão liberada.
- O processo é rápido e acontece em poucos segundos, sem necessidade de ações adicionais pelo colaborador.
- É possível visualizar as fotos salvas pelo reconhecimento facial diretamente na [folha de ponto do colaborador](https://app.crisp.chat/website/700f79b5-d725-4f7d-8a35-fefab8c77bee/helpdesk/articles/pt-br/7641e4bc-4499-403c-8882-edfc1ff0dc44/).

---

O reconhecimento facial traz mais segurança e confiabilidade ao registro de ponto, garantindo que apenas o próprio colaborador consiga validar sua jornada. Esse recurso é simples de usar, acontece de forma automática no momento da batida de ponto e pode ser configurado de acordo com a política de cada empresa.

Se precisar de apoio para habilitar ou ajustar essa funcionalidade, consulte o artigo complementar de [configuração e gestão do reconhecimento facial](https://sankhya.zendesk.com/hc/pt-br/articles/42427252165271) ou fale com nosso time de suporte pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
