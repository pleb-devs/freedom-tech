# freedom-tech

Suggested list of secure, adversarial, and otherwise freedom focused technologies, packages, and libraries to utilize for building sovereign apps.

This is all just tech that I know and use! There are many other amazing options that I am ignorant to!

## How this catalog is organized

* **By Topic** → Bitcoin, Lightning, Ecash, Networking/Privacy, Storage/Sync, Messaging/Comms, Nostr,
  Cryptography, Auth/Sessions
* **By Type** → Libraries/SDKs, Runtimes/Servers, Tools/CLIs, Protocols/Standards
* **By Language** → JavaScript/TypeScript, Rust, Go, Python, Multi-lang
* **By Use Case** → Key mgmt, wallets, relays, signing, descriptors/miniscript, transport privacy, sessions, WebAuthn/Passkeys, etc.
* **App Frameworks** → Desktop-native shells for JS frontends (e.g., Tauri)

> **Entry format**: `Name` – short note *(Language • Type • Topic • Use cases)* — [link]

---

## Quick Index

* [By Topic](#by-topic)
* [By Type](#by-type)
* [App Frameworks](#app-frameworks)
* [By Language](#by-language)
* [Tag Glossary](#tag-glossary)

---

## By Topic

### Bitcoin

* **BDK** (Bitcoin Dev Kit) – Wallet & chain access toolkit *(Rust • Library • Bitcoin • wallets, descriptors)* — [https://bitcoindevkit.org/](https://bitcoindevkit.org/)
* **Bitcoin Core** – Reference full node & wallet daemon *(C/C++ • Server • Bitcoin • validation, RPC, wallets)* — [https://bitcoincore.org/](https://bitcoincore.org/)
* **bitcoinjs-lib** – Bitcoin primitives & tx building *(JS/TS • Library • Bitcoin • tx building, PSBT)* — [https://github.com/bitcoinjs/bitcoinjs-lib](https://github.com/bitcoinjs/bitcoinjs-lib)
* **bitcoinerlab/descriptors** – Output descriptors parsing/building *(JS/TS • Library • Bitcoin • descriptors)* — [https://github.com/bitcoinerlab/descriptors](https://github.com/bitcoinerlab/descriptors)
* **btcd** – Full node implementation *(Go • Server • Bitcoin • validation, RPC)* — [https://github.com/btcsuite/btcd](https://github.com/btcsuite/btcd)
* **electrs** – Electrum server (indexer) for your own wallets *(Rust • Server • Bitcoin • indexing, wallet queries)* — [https://github.com/romanz/electrs](https://github.com/romanz/electrs)
* **HWI** (Hardware Wallet Interface) – Standard CLI/lib for PSBT with hardware wallets *(Python • Tool/CLI • Bitcoin • PSBT, descriptors)* — [https://github.com/bitcoin-core/HWI](https://github.com/bitcoin-core/HWI)
* **JoinMarket** – CoinJoin coordinator + market maker *(Python • Tool/CLI • Bitcoin • coinjoin, liquidity)* — [https://github.com/JoinMarket-Org/joinmarket-clientserver](https://github.com/JoinMarket-Org/joinmarket-clientserver)
* **rust-bitcoin** – Core Bitcoin types *(Rust • Library • Bitcoin • primitives)* — [https://github.com/rust-bitcoin/rust-bitcoin](https://github.com/rust-bitcoin/rust-bitcoin)
* **rust-miniscript** – Miniscript & descriptors *(Rust • Library • Bitcoin • miniscript, policy)* — [https://github.com/rust-bitcoin/rust-miniscript](https://github.com/rust-bitcoin/rust-miniscript)
* **scure-base** – bech32/base58/base64 *(JS/TS • Library • Crypto/Bitcoin • encodings)* — [https://github.com/paulmillr/scure-base](https://github.com/paulmillr/scure-base)
* **scure-bip32** – HD derivation *(JS/TS • Library • Crypto/Bitcoin • key derivation)* — [https://github.com/paulmillr/scure-bip32](https://github.com/paulmillr/scure-bip32)
* **scure-bip39** – Mnemonics *(JS/TS • Library • Crypto/Bitcoin • seed generation)* — [https://github.com/paulmillr/scure-bip39](https://github.com/paulmillr/scure-bip39)
* **scure-btc-signer** – Lightweight PSBT/signing *(JS/TS • Library • Bitcoin • signer)* — [https://github.com/paulmillr/scure-btc-signer](https://github.com/paulmillr/scure-btc-signer)

### Lightning

* **Core Lightning (CLN)** – Lightning node *(C • Server • Lightning • node operations)* — [https://github.com/ElementsProject/lightning](https://github.com/ElementsProject/lightning)
* **LDK** – Lightning Dev Kit *(Rust • Library • Lightning • node/wallet, routing)* — [https://lightningdevkit.org/](https://lightningdevkit.org/)
* **LDK Node** – Single-binary Lightning node API atop LDK *(Rust • Library • Lightning • node bootstrap, background tasks)* — [https://github.com/lightningdevkit/ldk-node](https://github.com/lightningdevkit/ldk-node)
* **LND** – Lightning node with gRPC & REST *(Go • Server • Lightning • node, APIs)* — [https://github.com/lightningnetwork/lnd](https://github.com/lightningnetwork/lnd)
* **LNbits** – Extensible Lightning accounts server *(Python • Server • Lightning • custodial wallets, extensions)* — [https://github.com/lnbits/lnbits](https://github.com/lnbits/lnbits)
* **Validating Lightning Signer (VLS)** – Remote signer for Lightning nodes *(Rust • Library • Lightning • stateless node signer, HSM-style)* — [https://vls.tech/](https://vls.tech/)
* **tonic_lnd** – gRPC client for LND *(Rust • Library • Lightning • API client)* — [https://github.com/Kixunil/tonic_lnd](https://github.com/Kixunil/tonic_lnd)

### Ecash

* **Cashu** – Reference Chaumian e-cash mint & wallet *(Python • Tool/CLI • Ecash • bearer tokens, ecash)* — [https://github.com/cashubtc/nutshell](https://github.com/cashubtc/nutshell)
* **Fedimint** – Modular federated e-cash backend *(Rust • Server • Ecash • community custody, e-cash)* — [https://github.com/fedimint/fedimint](https://github.com/fedimint/fedimint)

### Networking / Privacy

* **Bitchat** – Offline-first Bluetooth/Nostr messenger *(Swift/Kotlin • Tool/CLI • Networking/Privacy • mesh messaging)* — [https://github.com/BitChatLib/BitChat](https://github.com/BitChatLib/BitChat)
* **cjdns** – Encrypted IPv6 mesh networking stack *(C • Server • Networking/Privacy • mesh routing, IP allocation)* — [https://github.com/cjdelisle/cjdns](https://github.com/cjdelisle/cjdns)
* **I2P** – Anonymous overlay network *(Java • Server • Networking/Privacy • traffic hiding, tunnels)* — [https://geti2p.net/](https://geti2p.net/)
* **Snowflake** – Pluggable transport proxy for Tor *(Go • Server • Networking/Privacy • traffic obfuscation)* — [https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/snowflake](https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/snowflake)
* **Tailscale** – Managed WireGuard mesh with SSO & ACLs *(Go • Tool/CLI • Networking/Privacy • overlay VPN)* — [https://tailscale.com/kb/1017/what-is-tailscale](https://tailscale.com/kb/1017/what-is-tailscale)
* **Tor** – Onion routing daemon *(C • Server • Networking/Privacy • anonymity network)* — [https://gitlab.torproject.org/tpo/core/tor](https://gitlab.torproject.org/tpo/core/tor)
* **WireGuard** – Minimal VPN toolkit *(C • Tool/CLI • Networking/Privacy • tunnels)* — [https://www.wireguard.com/](https://www.wireguard.com/)
* **Syncthing** – Encrypted P2P file sync *(Go • Tool/CLI • Networking/Privacy • file sync, LAN/mesh)* — [https://syncthing.net/](https://syncthing.net/)
* **Yggdrasil** – Global encrypted mesh overlay *(Go • Server • Networking/Privacy • IPv6 routing)* — [https://yggdrasil-network.github.io/](https://yggdrasil-network.github.io/)

### Storage / Sync

* **Automerge** – Local-first CRDT document store *(JS/TS • Library • Storage/Sync • offline edits, sync, merge)* — [https://github.com/automerge/automerge](https://github.com/automerge/automerge)
* **Yjs** – CRDT framework for collaborative data *(JS/TS • Library • Storage/Sync • shared docs, presence)* — [https://github.com/yjs/yjs](https://github.com/yjs/yjs)

### Messaging / Comms

* **Bitchat** – Offline-first Bluetooth/Nostr messenger *(Swift/Kotlin • Tool/CLI • Messaging/Comms • mesh chat)* — [https://github.com/BitChatLib/BitChat](https://github.com/BitChatLib/BitChat)
* **Signal Protocol** – E2EE messaging protocol *(Spec • Protocol/Standard • Messaging/Comms • e2ee, ratchets)* — [https://signal.org/docs/](https://signal.org/docs/)

### Nostr

* **go-nostr** – Nostr Go toolkit *(Go • Library • Nostr • client)* — [https://github.com/nbd-wtf/go-nostr](https://github.com/nbd-wtf/go-nostr)
* **NDK** – Nostr Dev Kit *(JS/TS • Library • Nostr • client, abstractions)* — [https://github.com/nostr-dev-kit/ndk](https://github.com/nostr-dev-kit/ndk)
* **NIP-44** – Nostr encrypted DMs *(Spec • Protocol/Standard • Nostr • encryption)* — [https://github.com/paulmillr/nip44](https://github.com/paulmillr/nip44)
* **nostr-rs-relay** – High-performance relay *(Rust • Server • Nostr • relay)* — [https://github.com/scsibug/nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay)
* **nostr-tools** – Client utils *(JS/TS • Library • Nostr • keys, events, relays)* — [https://github.com/nbd-wtf/nostr-tools](https://github.com/nbd-wtf/nostr-tools)
* **relayer** – Nostr relay framework *(Go • Server • Nostr • framework)* — [https://github.com/fiatjaf/relayer](https://github.com/fiatjaf/relayer)
* **rust-nostr** – Nostr types & client *(Rust • Library • Nostr • client, events)* — [https://github.com/rust-nostr/nostr](https://github.com/rust-nostr/nostr)
* **SNSTR** – Minimal Nostr toolkit *(JS/TS • Library • Nostr • ergonomics)* — [https://github.com/austinkelsay/snstr](https://github.com/austinkelsay/snstr)
* **strfry** – High-performance Nostr relay using LMDB *(C/C++ • Server • Nostr • relay)* — [https://github.com/hoytech/strfry](https://github.com/hoytech/strfry)

### Cryptography

* **@noble/ciphers** – Stream & AEAD primitives *(JS/TS • Library • Crypto • ChaCha20-Poly1305, etc.)* — [https://github.com/paulmillr/noble-ciphers](https://github.com/paulmillr/noble-ciphers)
* **@noble/curves** – Pure JS curves *(JS/TS • Library • Crypto • secp256k1/ed25519)* — [https://github.com/paulmillr/noble-curves](https://github.com/paulmillr/noble-curves)
* **@noble/hashes** – Hash suites *(JS/TS • Library • Crypto • SHA-256, Blake3, etc.)* — [https://github.com/paulmillr/noble-hashes](https://github.com/paulmillr/noble-hashes)
* **@noble/post-quantum** – PQ experiments *(JS/TS • Library • Crypto • PQ signatures)* — [https://github.com/paulmillr/noble-post-quantum](https://github.com/paulmillr/noble-post-quantum)
* **age** – Modern file encryption (format + CLI + Go lib) *(Go • Tool/CLI • Crypto • file encryption, key wrapping)* — [https://github.com/FiloSottile/age](https://github.com/FiloSottile/age)
* **libsodium** – Modern crypto primitives bundle *(C • Library • Crypto • AEAD, signatures, KDF)* — [https://github.com/jedisct1/libsodium](https://github.com/jedisct1/libsodium)
* **libsecp256k1** – secp256k1 curve implementation *(C • Library • Crypto • ECDSA, Schnorr)* — [https://github.com/bitcoin-core/secp256k1](https://github.com/bitcoin-core/secp256k1)
* **minisign** – Dead-simple file signing & verification (Ed25519) *(C • Tool/CLI • Crypto • release signing)* — [https://github.com/jedisct1/minisign](https://github.com/jedisct1/minisign)
* **scure-base** – bech32/base58/base64 *(JS/TS • Library • Crypto • encodings)* — [https://github.com/paulmillr/scure-base](https://github.com/paulmillr/scure-base)
* **scure-bip32** – HD derivation *(JS/TS • Library • Crypto/Bitcoin • key derivation)* — [https://github.com/paulmillr/scure-bip32](https://github.com/paulmillr/scure-bip32)
* **scure-bip39** – Mnemonics *(JS/TS • Library • Crypto/Bitcoin • seed generation)* — [https://github.com/paulmillr/scure-bip39](https://github.com/paulmillr/scure-bip39)
* **scure-btc-signer** – Lightweight PSBT/signing *(JS/TS • Library • Crypto/Bitcoin • signer)* — [https://github.com/paulmillr/scure-btc-signer](https://github.com/paulmillr/scure-btc-signer)

### Auth / Sessions

* **iron-session** – Stateless encrypted cookies *(JS/TS • Library • Auth • session storage)* — [https://github.com/vvo/iron-session](https://github.com/vvo/iron-session)
* **simplewebauthn** – WebAuthn/Passkeys server & browser *(JS/TS • Library • Auth • passkeys)* — [https://github.com/MasterKale/SimpleWebAuthn](https://github.com/MasterKale/SimpleWebAuthn)

---

## By Type

### Libraries / SDKs

* **@noble/ciphers** – Stream & AEAD *(JS/TS • Library • Crypto • ChaCha20-Poly1305, etc.)* — [https://github.com/paulmillr/noble-ciphers](https://github.com/paulmillr/noble-ciphers)
* **@noble/curves** – Pure JS curves *(JS/TS • Library • Crypto • secp256k1/ed25519)* — [https://github.com/paulmillr/noble-curves](https://github.com/paulmillr/noble-curves)
* **@noble/hashes** – Hash suites *(JS/TS • Library • Crypto • SHA-256, Blake3, etc.)* — [https://github.com/paulmillr/noble-hashes](https://github.com/paulmillr/noble-hashes)
* **@noble/post-quantum** – PQ experiments *(JS/TS • Library • Crypto)* — [https://github.com/paulmillr/noble-post-quantum](https://github.com/paulmillr/noble-post-quantum)
* **BDK** (Bitcoin Dev Kit) – Wallet & chain access toolkit *(Rust • Library • Bitcoin • wallets, descriptors)* — [https://bitcoindevkit.org/](https://bitcoindevkit.org/)
* **bitcoinjs-lib** – Bitcoin primitives & tx building *(JS/TS • Library • Bitcoin • tx building, PSBT)* — [https://github.com/bitcoinjs/bitcoinjs-lib](https://github.com/bitcoinjs/bitcoinjs-lib)
* **bitcoinerlab/descriptors** – Output descriptors parsing/building *(JS/TS • Library • Bitcoin • descriptors)* — [https://github.com/bitcoinerlab/descriptors](https://github.com/bitcoinerlab/descriptors)
* **go-nostr** – Nostr Go toolkit *(Go • Library • Nostr • client)* — [https://github.com/nbd-wtf/go-nostr](https://github.com/nbd-wtf/go-nostr)
* **LDK** – Lightning Dev Kit *(Rust • Library • Lightning • node/wallet, routing)* — [https://lightningdevkit.org/](https://lightningdevkit.org/)
* **LDK Node** – Single-binary Lightning node API atop LDK *(Rust • Library • Lightning • node bootstrap, background tasks)* — [https://github.com/lightningdevkit/ldk-node](https://github.com/lightningdevkit/ldk-node)
* **libsodium** – Modern crypto primitives bundle *(C • Library • Crypto • AEAD, signatures, KDF)* — [https://github.com/jedisct1/libsodium](https://github.com/jedisct1/libsodium)
* **libsecp256k1** – secp256k1 curve impl *(C • Library • Crypto • ECDSA, Schnorr)* — [https://github.com/bitcoin-core/secp256k1](https://github.com/bitcoin-core/secp256k1)
* **NDK** – Nostr Dev Kit *(JS/TS • Library • Nostr • client, abstractions)* — [https://github.com/nostr-dev-kit/ndk](https://github.com/nostr-dev-kit/ndk)
* **nostr-tools** – Client utils *(JS/TS • Library • Nostr • keys, events, relay)* — [https://github.com/nbd-wtf/nostr-tools](https://github.com/nbd-wtf/nostr-tools)
* **rust-bitcoin** – Core Bitcoin types *(Rust • Library • Bitcoin • primitives)* — [https://github.com/rust-bitcoin/rust-bitcoin](https://github.com/rust-bitcoin/rust-bitcoin)
* **rust-miniscript** – Miniscript & descriptors *(Rust • Library • Bitcoin • miniscript, policy)* — [https://github.com/rust-bitcoin/rust-miniscript](https://github.com/rust-bitcoin/rust-miniscript)
* **rust-nostr** – Nostr types & client *(Rust • Library • Nostr • client, events)* — [https://github.com/rust-nostr/nostr](https://github.com/rust-nostr/nostr)
* **scure-base** – bech32/base58/base64 *(JS/TS • Library • Crypto • encodings)* — [https://github.com/paulmillr/scure-base](https://github.com/paulmillr/scure-base)
* **scure-bip32** – HD derivation *(JS/TS • Library • Crypto/Bitcoin • key derivation)* — [https://github.com/paulmillr/scure-bip32](https://github.com/paulmillr/scure-bip32)
* **scure-bip39** – Mnemonics *(JS/TS • Library • Crypto/Bitcoin • seed gen)* — [https://github.com/paulmillr/scure-bip39](https://github.com/paulmillr/scure-bip39)
* **scure-btc-signer** – Lightweight PSBT/signing *(JS/TS • Library • Bitcoin • signer)* — [https://github.com/paulmillr/scure-btc-signer](https://github.com/paulmillr/scure-btc-signer)
* **simplewebauthn** – WebAuthn/Passkeys server & browser *(JS/TS • Library • Auth • passkeys)* — [https://github.com/MasterKale/SimpleWebAuthn](https://github.com/MasterKale/SimpleWebAuthn)
* **SNSTR** – Minimal Nostr toolkit *(JS/TS • Library • Nostr • client, ergonomics)* — [https://github.com/austinkelsay/snstr](https://github.com/austinkelsay/snstr)
* **tonic_lnd** – gRPC client for LND *(Rust • Library • Lightning • API client)* — [https://github.com/Kixunil/tonic_lnd](https://github.com/Kixunil/tonic_lnd)

### Runtimes / Servers

* **btcd** – Full node implementation *(Go • Server • Bitcoin)* — [https://github.com/btcsuite/btcd](https://github.com/btcsuite/btcd)
* **Core Lightning (CLN)** – Lightning node *(C • Server • Lightning)* — [https://github.com/ElementsProject/lightning](https://github.com/ElementsProject/lightning)
* **electrs** – Electrum server (indexer) for your own wallets *(Rust • Server • Bitcoin • indexing, wallet queries)* — [https://github.com/romanz/electrs](https://github.com/romanz/electrs)
* **Fedimint** – Modular federated e-cash backend *(Rust • Server • Ecash • community custody, e-cash)* — [https://github.com/fedimint/fedimint](https://github.com/fedimint/fedimint)
* **LNbits** – Extensible Lightning accounts server *(Python • Server • Lightning • custodial wallets, extensions)* — [https://github.com/lnbits/lnbits](https://github.com/lnbits/lnbits)
* **LND** – Lightning node w/ gRPC & REST *(Go • Server • Lightning • node, APIs)* — [https://github.com/lightningnetwork/lnd](https://github.com/lightningnetwork/lnd)
* **nostr-rs-relay** – High-perf relay *(Rust • Server • Nostr)* — [https://github.com/scsibug/nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay)
* **relayer** – Nostr relay framework *(Go • Server • Nostr)* — [https://github.com/fiatjaf/relayer](https://github.com/fiatjaf/relayer)
* **I2P** – Anonymous overlay network *(Java • Server • Networking/Privacy • traffic hiding, tunnels)* — [https://geti2p.net/](https://geti2p.net/)
* **Snowflake** – Pluggable transport proxy for Tor *(Go • Server • Networking/Privacy • traffic obfuscation)* — [https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/snowflake](https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/snowflake)
* **strfry** – High-performance Nostr relay using LMDB *(C/C++ • Server • Nostr • relay)* — [https://github.com/hoytech/strfry](https://github.com/hoytech/strfry)
* **Tor** – Onion routing daemon *(C • Server • Networking/Privacy • anonymity network)* — [https://gitlab.torproject.org/tpo/core/tor](https://gitlab.torproject.org/tpo/core/tor)
* **Yggdrasil** – Global encrypted mesh overlay *(Go • Server • Networking/Privacy • IPv6 routing)* — [https://yggdrasil-network.github.io/](https://yggdrasil-network.github.io/)

### Protocols / Standards

* **NIP-44** – Nostr encrypted DMs *(Spec • Protocol/Standard • Nostr • encryption)* — [https://github.com/paulmillr/nip44](https://github.com/paulmillr/nip44)
* **Signal Protocol** – E2EE messaging protocol *(Spec • Protocol/Standard • Messaging/Comms • e2ee, ratchets)* — [https://signal.org/docs/](https://signal.org/docs/)

### Tools / CLIs

* **age** – Modern file encryption (format + CLI + Go lib) *(Go • Tool/CLI • Crypto • file encryption, key wrapping)* — [https://github.com/FiloSottile/age](https://github.com/FiloSottile/age)
* **Bitchat** – Offline-first Bluetooth/Nostr messenger *(Swift/Kotlin • Tool/CLI • Networking/Privacy • adhoc comms)* — [https://github.com/BitChatLib/BitChat](https://github.com/BitChatLib/BitChat)
* **Cashu** – Reference Chaumian e-cash mint & wallet *(Python • Tool/CLI • Ecash • bearer tokens, ecash)* — [https://github.com/cashubtc/nutshell](https://github.com/cashubtc/nutshell)
* **HWI** (Hardware Wallet Interface) – Standard CLI/lib for PSBT w/ hardware wallets *(Python • Tool/CLI • Bitcoin • PSBT, descriptors)* — [https://github.com/bitcoin-core/HWI](https://github.com/bitcoin-core/HWI)
* **JoinMarket** – CoinJoin coordinator + market maker *(Python • Tool/CLI • Bitcoin • coinjoin, liquidity)* — [https://github.com/JoinMarket-Org/joinmarket-clientserver](https://github.com/JoinMarket-Org/joinmarket-clientserver)
* **minisign** – Dead-simple file signing & verification (Ed25519) *(C • Tool/CLI • Crypto • release signing)* — [https://github.com/jedisct1/minisign](https://github.com/jedisct1/minisign)
* **Syncthing** – Encrypted P2P file sync *(Go • Tool/CLI • Networking/Privacy • file sync, LAN/mesh)* — [https://syncthing.net/](https://syncthing.net/)
* **Tailscale** – Managed WireGuard mesh with SSO & ACLs *(Go • Tool/CLI • Networking/Privacy • overlay VPN)* — [https://tailscale.com/kb/1017/what-is-tailscale](https://tailscale.com/kb/1017/what-is-tailscale)
* **WireGuard** – Minimal VPN toolkit *(C • Tool/CLI • Networking/Privacy • tunnels)* — [https://www.wireguard.com/](https://www.wireguard.com/)

---

## App Frameworks

* **Tauri** – Webview shell *(Rust/JS • Framework • App • desktop)* — [tauri.app](https://tauri.app)
* **Wails** – Go webview shell *(Go/JS • Framework • App • desktop)* — [wails.io](https://wails.io)

---

## By Language

### JavaScript / TypeScript

* **bitcoinjs-lib**, **bitcoinerlab/descriptors** *(Bitcoin)*
* **NDK**, **nostr-tools**, **SNSTR** *(Nostr)*
* **@noble/**, **scure-/** *(Crypto)*
* **iron-session**, **simplewebauthn** *(Auth)*
* **Automerge**, **Yjs** *(Storage/Sync)*

### Rust

* **BDK**, **rust-bitcoin**, **rust-miniscript** *(Bitcoin)*
* **LDK**, **LDK Node**, **tonic_lnd** *(Lightning)*
* **Fedimint** *(Ecash)*
* **rust-nostr** *(Nostr)*
* **nostr-rs-relay** *(Server)*
* **electrs** *(Server/indexer)*
* **Validating Lightning Signer (VLS)** *(Lightning signer)*

### Go

* **btcd** *(Bitcoin server)*
* **go-nostr** *(Nostr lib)*
* **LND** *(Lightning server)*
* **relayer** *(Nostr server framework)*
* **Snowflake**, **Tailscale**, **Yggdrasil** *(Networking/Privacy)*
* **Syncthing** *(Networking/Privacy file sync)*
* **Wails** *(App framework)*

### C / C++

* **Core Lightning (CLN)** *(Lightning server)*
* **libsecp256k1** *(Crypto)*
* **libsodium** *(Crypto)*
* **minisign** *(Tool/CLI)*
* **strfry** *(Nostr server)*
* **Tor**, **WireGuard** *(Networking/Privacy)*
* **Bitcoin Core**, **cjdns** *(Bitcoin, Networking/Privacy)*

### Java

* **I2P** *(Networking/Privacy overlay)*

### Python

* **Cashu**, **HWI**, **JoinMarket**, **LNbits** *(Tool/CLI & Server)*

### Multi-lang

* **Bitchat** *(Networking/Privacy messenger)*

---

## Tag Glossary

* **Type**: Library, Server (Runtime), Tool/CLI, Protocol/Standard, Framework
* **Topic**: Bitcoin, Lightning, Ecash, Nostr, Crypto, Auth, Networking/Privacy, Storage/Sync,
  Messaging/Comms, App
* **Language**: JS/TS, Rust, Go, C/C++, Java, Python, Multi, Spec
* **Use cases**: wallets, descriptors/miniscript, tx/PSBT, relays, node, routing, encryption, passkeys,
  sessions, file sync, anonymity overlays, desktop

---

## Roadmap for next expansion

* Expand **Networking/Privacy** coverage (e.g., I2P, mixnets) and add more **Tools/CLIs**
* Add **Storage/Sync** options (local-first/CRDTs) where relevant to sovereignty
* Add quick **comparison tables** (features, licenses, maintenance) as the catalog grows
