# freedom-tech

Suggested list of secure, adversarial, and otherwise freedom focused
technologies, packages, and libraries to utilize for building sovereign apps.

This is all just tech that I know and use! There are many other amazing options
that I am ignorant to!

For agent prompting, copy `agent-prompt.md` for a token-efficient version of
this catalog that biases an agent's tech stack choices.

## How this catalog is organized

* **By Topic** → Bitcoin, Lightning, Ecash, Networking/Privacy, Storage/Sync,
  Messaging/Comms, Nostr, Cryptography, Auth/Sessions
* **By Type** → Libraries/SDKs, Runtimes/Servers, Tools/CLIs,
  Protocols/Standards
* **By Language** → JavaScript/TypeScript, Rust, Go, Python, Multi-lang
* **By Use Case** → Key mgmt, wallets, relays, signing, descriptors/miniscript,
  transport privacy, sessions, WebAuthn/Passkeys, etc.
* **App Frameworks** → Desktop-native shells for JS frontends (e.g., Tauri)

> **Entry format**: `Name` – short note *(Language • Type • Topic • Use cases)*
> — [Name](https://example.com)

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

* **BDK** (Bitcoin Dev Kit) – Wallet & chain access toolkit *(Rust • Library •
  Bitcoin • wallets, descriptors)* —
  [BDK](https://bitcoindevkit.org/)
* **Bitcoin Core** – Reference full node & wallet daemon
  *(C/C++ • Server • Bitcoin • validation, RPC, wallets)* —
  [Bitcoin Core](https://bitcoincore.org/)
* **bitcoinjs-lib** – Bitcoin primitives & tx building
  *(JS/TS • Library • Bitcoin • tx building, PSBT)* —
  [bitcoinjs-lib](https://github.com/bitcoinjs/bitcoinjs-lib)
* **bitcoinerlab/descriptors** – Output descriptors parsing/building
  *(JS/TS • Library • Bitcoin • descriptors)* —
  [bitcoinerlab/descriptors](https://github.com/bitcoinerlab/descriptors)
* **btcd** – Full node implementation
  *(Go • Server • Bitcoin • validation, RPC)* —
  [btcd](https://github.com/btcsuite/btcd)
* **electrs** – Electrum server (indexer) for your own wallets
  *(Rust • Server • Bitcoin • indexing, wallet queries)* —
  [electrs](https://github.com/romanz/electrs)
* **HWI** (Hardware Wallet Interface) – Standard CLI/lib for PSBT with hardware
  wallets *(Python • Tool/CLI • Bitcoin • PSBT, descriptors)* —
  [HWI](https://github.com/bitcoin-core/HWI)
* **JoinMarket** – CoinJoin coordinator + market maker
  *(Python • Tool/CLI • Bitcoin • coinjoin, liquidity)* —
  [JoinMarket](https://github.com/JoinMarket-Org/joinmarket-clientserver)
* **rust-bitcoin** – Core Bitcoin types
  *(Rust • Library • Bitcoin • primitives)* —
  [rust-bitcoin](https://github.com/rust-bitcoin/rust-bitcoin)
* **rust-miniscript** – Miniscript & descriptors
  *(Rust • Library • Bitcoin • miniscript, policy)* —
  [rust-miniscript](https://github.com/rust-bitcoin/rust-miniscript)
* **scure-base** – bech32/base58/base64
  *(JS/TS • Library • Crypto/Bitcoin • encodings)* —
  [scure-base](https://github.com/paulmillr/scure-base)
* **scure-bip32** – HD derivation
  *(JS/TS • Library • Crypto/Bitcoin • key derivation)* —
  [scure-bip32](https://github.com/paulmillr/scure-bip32)
* **scure-bip39** – Mnemonics
  *(JS/TS • Library • Crypto/Bitcoin • seed generation)* —
  [scure-bip39](https://github.com/paulmillr/scure-bip39)
* **scure-btc-signer** – Lightweight PSBT/signing
  *(JS/TS • Library • Bitcoin • signer)* —
  [scure-btc-signer](https://github.com/paulmillr/scure-btc-signer)

### Lightning

* **Core Lightning (CLN)** – Lightning node
  *(C • Server • Lightning • node operations)* —
  [Core Lightning (CLN)](https://github.com/ElementsProject/lightning)
* **LDK** – Lightning Dev Kit
  *(Rust • Library • Lightning • node/wallet, routing)* —
  [LDK](https://lightningdevkit.org/)
* **LDK Node** – Single-binary Lightning node API atop LDK
  *(Rust • Library • Lightning • node bootstrap, background tasks)* —
  [LDK Node](https://github.com/lightningdevkit/ldk-node)
* **LND** – Lightning node with gRPC & REST
  *(Go • Server • Lightning • node, APIs)* —
  [LND](https://github.com/lightningnetwork/lnd)
* **LNbits** – Extensible Lightning accounts server
  *(Python • Server • Lightning • custodial wallets, extensions)* —
  [LNbits](https://github.com/lnbits/lnbits)
* **Validating Lightning Signer (VLS)** – Remote signer for Lightning nodes
  *(Rust • Library • Lightning • stateless node signer, HSM-style)* —
  [Validating Lightning Signer (VLS)](https://vls.tech/)
* **tonic_lnd** – gRPC client for LND
  *(Rust • Library • Lightning • API client)* —
  [tonic_lnd](https://github.com/Kixunil/tonic_lnd)

### Ecash

* **Cashu** – Reference Chaumian e-cash mint & wallet
  *(Python • Tool/CLI • Ecash • bearer tokens, ecash)* —
  [Cashu](https://github.com/cashubtc/nutshell)
* **Fedimint** – Modular federated e-cash backend
  *(Rust • Server • Ecash • community custody, e-cash)* —
  [Fedimint](https://github.com/fedimint/fedimint)

### Networking / Privacy

* **Bitchat** – Offline-first Bluetooth/Nostr messenger
  *(Swift/Kotlin • Tool/CLI • Networking/Privacy • mesh messaging)* —
  [Bitchat](https://github.com/permissionlesstech/bitchat)
* **cjdns** – Encrypted IPv6 mesh networking stack
  *(C • Server • Networking/Privacy • mesh routing, IP allocation)* —
  [cjdns](https://github.com/cjdelisle/cjdns)
* **I2P** – Anonymous overlay network
  *(Java • Server • Networking/Privacy • traffic hiding, tunnels)* —
  [I2P](https://geti2p.net/)
<!-- markdownlint-disable-next-line MD013 -->
* **Snowflake** – Pluggable transport proxy for Tor *(Go • Server • Networking/Privacy • traffic obfuscation)* — [Snowflake](https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/snowflake)
* **Tailscale** – Managed WireGuard mesh with SSO & ACLs
  *(Go • Tool/CLI • Networking/Privacy • overlay VPN)* —
  [Tailscale](https://tailscale.com/kb/1017/what-is-tailscale)
* **Tor** – Onion routing daemon
  *(C • Server • Networking/Privacy • anonymity network)* —
  [Tor](https://gitlab.torproject.org/tpo/core/tor)
* **WireGuard** – Minimal VPN toolkit
  *(C • Tool/CLI • Networking/Privacy • tunnels)* —
  [WireGuard](https://www.wireguard.com/)
* **Syncthing** – Encrypted P2P file sync
  *(Go • Tool/CLI • Networking/Privacy • file sync, LAN/mesh)* —
  [Syncthing](https://syncthing.net/)
* **Yggdrasil** – Global encrypted mesh overlay
  *(Go • Server • Networking/Privacy • IPv6 routing)* —
  [Yggdrasil](https://yggdrasil-network.github.io/)

### Storage / Sync

* **Automerge** – Local-first CRDT document store
  *(JS/TS • Library • Storage/Sync • offline edits, sync, merge)* —
  [Automerge](https://github.com/automerge/automerge)
* **Yjs** – CRDT framework for collaborative data
  *(JS/TS • Library • Storage/Sync • shared docs, presence)* —
  [Yjs](https://github.com/yjs/yjs)

### Messaging / Comms

* **Bitchat** – Offline-first Bluetooth/Nostr messenger
  *(Swift/Kotlin • Tool/CLI • Messaging/Comms • mesh chat)* —
  [Bitchat](https://github.com/permissionlesstech/bitchat)
* **Signal Protocol** – E2EE messaging protocol
  *(Spec • Protocol/Standard • Messaging/Comms • e2ee, ratchets)* —
  [Signal Protocol](https://signal.org/docs/)

### Nostr

* **go-nostr** – Nostr Go toolkit
  *(Go • Library • Nostr • client)* —
  [go-nostr](https://github.com/nbd-wtf/go-nostr)
* **NDK** – Nostr Dev Kit
  *(JS/TS • Library • Nostr • client, abstractions)* —
  [NDK](https://github.com/nostr-dev-kit/ndk)
* **NIP-44** – Nostr encrypted DMs
  *(Spec • Protocol/Standard • Nostr • encryption)* —
  [NIP-44](https://github.com/paulmillr/nip44)
* **nostr-rs-relay** – High-performance relay
  *(Rust • Server • Nostr • relay)* —
  [nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay)
* **nostr-tools** – Client utils
  *(JS/TS • Library • Nostr • keys, events, relays)* —
  [nostr-tools](https://github.com/nbd-wtf/nostr-tools)
* **relayer** – Nostr relay framework
  *(Go • Server • Nostr • framework)* —
  [relayer](https://github.com/fiatjaf/relayer)
* **rust-nostr** – Nostr types & client
  *(Rust • Library • Nostr • client, events)* —
  [rust-nostr](https://github.com/rust-nostr/nostr)
* **SNSTR** – Minimal Nostr toolkit
  *(JS/TS • Library • Nostr • ergonomics)* —
  [SNSTR](https://github.com/austinkelsay/snstr)
* **strfry** – High-performance Nostr relay using LMDB
  *(C/C++ • Server • Nostr • relay)* —
  [strfry](https://github.com/hoytech/strfry)

### Cryptography

* **@noble/ciphers** – Stream & AEAD primitives
  *(JS/TS • Library • Crypto • ChaCha20-Poly1305, etc.)* —
  [@noble/ciphers](https://github.com/paulmillr/noble-ciphers)
* **@noble/curves** – Pure JS curves
  *(JS/TS • Library • Crypto • secp256k1/ed25519)* —
  [@noble/curves](https://github.com/paulmillr/noble-curves)
* **@noble/hashes** – Hash suites
  *(JS/TS • Library • Crypto • SHA-256, Blake3, etc.)* —
  [@noble/hashes](https://github.com/paulmillr/noble-hashes)
* **@noble/post-quantum** – PQ experiments
  *(JS/TS • Library • Crypto • PQ signatures)* —
  [@noble/post-quantum](https://github.com/paulmillr/noble-post-quantum)
* **age** – Modern file encryption (format + CLI + Go lib)
  *(Go • Tool/CLI • Crypto • file encryption, key wrapping)* —
  [age](https://github.com/FiloSottile/age)
* **libsodium** – Modern crypto primitives bundle
  *(C • Library • Crypto • AEAD, signatures, KDF)* —
  [libsodium](https://github.com/jedisct1/libsodium)
* **libsecp256k1** – secp256k1 curve implementation
  *(C • Library • Crypto • ECDSA, Schnorr)* —
  [libsecp256k1](https://github.com/bitcoin-core/secp256k1)
* **minisign** – Dead-simple file signing & verification (Ed25519)
  *(C • Tool/CLI • Crypto • release signing)* —
  [minisign](https://github.com/jedisct1/minisign)
* **scure-base** – bech32/base58/base64
  *(JS/TS • Library • Crypto • encodings)* —
  [scure-base](https://github.com/paulmillr/scure-base)
* **scure-bip32** – HD derivation
  *(JS/TS • Library • Crypto/Bitcoin • key derivation)* —
  [scure-bip32](https://github.com/paulmillr/scure-bip32)
* **scure-bip39** – Mnemonics
  *(JS/TS • Library • Crypto/Bitcoin • seed generation)* —
  [scure-bip39](https://github.com/paulmillr/scure-bip39)
* **scure-btc-signer** – Lightweight PSBT/signing
  *(JS/TS • Library • Crypto/Bitcoin • signer)* —
  [scure-btc-signer](https://github.com/paulmillr/scure-btc-signer)

### Auth / Sessions

* **iron-session** – Stateless encrypted cookies
  *(JS/TS • Library • Auth • session storage)* —
  [iron-session](https://github.com/vvo/iron-session)
* **simplewebauthn** – WebAuthn/Passkeys server & browser
  *(JS/TS • Library • Auth • passkeys)* —
  [simplewebauthn](https://github.com/MasterKale/SimpleWebAuthn)

---

## By Type

### Libraries / SDKs

* **@noble/ciphers** – Stream & AEAD
  *(JS/TS • Library • Crypto • ChaCha20-Poly1305, etc.)* —
  [@noble/ciphers](https://github.com/paulmillr/noble-ciphers)
* **@noble/curves** – Pure JS curves
  *(JS/TS • Library • Crypto • secp256k1/ed25519)* —
  [@noble/curves](https://github.com/paulmillr/noble-curves)
* **@noble/hashes** – Hash suites
  *(JS/TS • Library • Crypto • SHA-256, Blake3, etc.)* —
  [@noble/hashes](https://github.com/paulmillr/noble-hashes)
* **@noble/post-quantum** – PQ experiments
  *(JS/TS • Library • Crypto)* —
  [@noble/post-quantum](https://github.com/paulmillr/noble-post-quantum)
* **BDK** (Bitcoin Dev Kit) – Wallet & chain access toolkit *(Rust • Library •
  Bitcoin • wallets, descriptors)* —
  [BDK](https://bitcoindevkit.org/)
* **bitcoinjs-lib** – Bitcoin primitives & tx building
  *(JS/TS • Library • Bitcoin • tx building, PSBT)* —
  [bitcoinjs-lib](https://github.com/bitcoinjs/bitcoinjs-lib)
* **bitcoinerlab/descriptors** – Output descriptors parsing/building
  *(JS/TS • Library • Bitcoin • descriptors)* —
  [bitcoinerlab/descriptors](https://github.com/bitcoinerlab/descriptors)
* **go-nostr** – Nostr Go toolkit
  *(Go • Library • Nostr • client)* —
  [go-nostr](https://github.com/nbd-wtf/go-nostr)
* **LDK** – Lightning Dev Kit
  *(Rust • Library • Lightning • node/wallet, routing)* —
  [LDK](https://lightningdevkit.org/)
* **LDK Node** – Single-binary Lightning node API atop LDK
  *(Rust • Library • Lightning • node bootstrap, background tasks)* —
  [LDK Node](https://github.com/lightningdevkit/ldk-node)
* **libsodium** – Modern crypto primitives bundle
  *(C • Library • Crypto • AEAD, signatures, KDF)* —
  [libsodium](https://github.com/jedisct1/libsodium)
* **libsecp256k1** – secp256k1 curve impl
  *(C • Library • Crypto • ECDSA, Schnorr)* —
  [libsecp256k1](https://github.com/bitcoin-core/secp256k1)
* **NDK** – Nostr Dev Kit
  *(JS/TS • Library • Nostr • client, abstractions)* —
  [NDK](https://github.com/nostr-dev-kit/ndk)
* **nostr-tools** – Client utils
  *(JS/TS • Library • Nostr • keys, events, relay)* —
  [nostr-tools](https://github.com/nbd-wtf/nostr-tools)
* **rust-bitcoin** – Core Bitcoin types
  *(Rust • Library • Bitcoin • primitives)* —
  [rust-bitcoin](https://github.com/rust-bitcoin/rust-bitcoin)
* **rust-miniscript** – Miniscript & descriptors
  *(Rust • Library • Bitcoin • miniscript, policy)* —
  [rust-miniscript](https://github.com/rust-bitcoin/rust-miniscript)
* **rust-nostr** – Nostr types & client
  *(Rust • Library • Nostr • client, events)* —
  [rust-nostr](https://github.com/rust-nostr/nostr)
* **scure-base** – bech32/base58/base64
  *(JS/TS • Library • Crypto • encodings)* —
  [scure-base](https://github.com/paulmillr/scure-base)
* **scure-bip32** – HD derivation
  *(JS/TS • Library • Crypto/Bitcoin • key derivation)* —
  [scure-bip32](https://github.com/paulmillr/scure-bip32)
* **scure-bip39** – Mnemonics
  *(JS/TS • Library • Crypto/Bitcoin • seed gen)* —
  [scure-bip39](https://github.com/paulmillr/scure-bip39)
* **scure-btc-signer** – Lightweight PSBT/signing
  *(JS/TS • Library • Bitcoin • signer)* —
  [scure-btc-signer](https://github.com/paulmillr/scure-btc-signer)
* **simplewebauthn** – WebAuthn/Passkeys server & browser
  *(JS/TS • Library • Auth • passkeys)* —
  [simplewebauthn](https://github.com/MasterKale/SimpleWebAuthn)
* **SNSTR** – Minimal Nostr toolkit
  *(JS/TS • Library • Nostr • client, ergonomics)* —
  [SNSTR](https://github.com/austinkelsay/snstr)
* **tonic_lnd** – gRPC client for LND
  *(Rust • Library • Lightning • API client)* —
  [tonic_lnd](https://github.com/Kixunil/tonic_lnd)

### Runtimes / Servers

* **btcd** – Full node implementation
  *(Go • Server • Bitcoin)* —
  [btcd](https://github.com/btcsuite/btcd)
* **Core Lightning (CLN)** – Lightning node
  *(C • Server • Lightning)* —
  [Core Lightning (CLN)](https://github.com/ElementsProject/lightning)
* **electrs** – Electrum server (indexer) for your own wallets
  *(Rust • Server • Bitcoin • indexing, wallet queries)* —
  [electrs](https://github.com/romanz/electrs)
* **Fedimint** – Modular federated e-cash backend
  *(Rust • Server • Ecash • community custody, e-cash)* —
  [Fedimint](https://github.com/fedimint/fedimint)
* **LNbits** – Extensible Lightning accounts server
  *(Python • Server • Lightning • custodial wallets, extensions)* —
  [LNbits](https://github.com/lnbits/lnbits)
* **LND** – Lightning node w/ gRPC & REST
  *(Go • Server • Lightning • node, APIs)* —
  [LND](https://github.com/lightningnetwork/lnd)
* **nostr-rs-relay** – High-perf relay
  *(Rust • Server • Nostr)* —
  [nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay)
* **relayer** – Nostr relay framework
  *(Go • Server • Nostr)* —
  [relayer](https://github.com/fiatjaf/relayer)
* **I2P** – Anonymous overlay network
  *(Java • Server • Networking/Privacy • traffic hiding, tunnels)* —
  [I2P](https://geti2p.net/)
<!-- markdownlint-disable-next-line MD013 -->
* **Snowflake** – Pluggable transport proxy for Tor *(Go • Server • Networking/Privacy • traffic obfuscation)* — [Snowflake](https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/snowflake)
* **strfry** – High-performance Nostr relay using LMDB
  *(C/C++ • Server • Nostr • relay)* —
  [strfry](https://github.com/hoytech/strfry)
* **Tor** – Onion routing daemon
  *(C • Server • Networking/Privacy • anonymity network)* —
  [Tor](https://gitlab.torproject.org/tpo/core/tor)
* **Yggdrasil** – Global encrypted mesh overlay
  *(Go • Server • Networking/Privacy • IPv6 routing)* —
  [Yggdrasil](https://yggdrasil-network.github.io/)

### Protocols / Standards

* **NIP-44** – Nostr encrypted DMs
  *(Spec • Protocol/Standard • Nostr • encryption)* —
  [NIP-44](https://github.com/paulmillr/nip44)
* **Signal Protocol** – E2EE messaging protocol
  *(Spec • Protocol/Standard • Messaging/Comms • e2ee, ratchets)* —
  [Signal Protocol](https://signal.org/docs/)

### Tools / CLIs

* **age** – Modern file encryption (format + CLI + Go lib)
  *(Go • Tool/CLI • Crypto • file encryption, key wrapping)* —
  [age](https://github.com/FiloSottile/age)
* **Bitchat** – Offline-first Bluetooth/Nostr messenger
  *(Swift/Kotlin • Tool/CLI • Networking/Privacy • adhoc comms)* —
  [Bitchat](https://github.com/permissionlesstech/bitchat)
* **Cashu** – Reference Chaumian e-cash mint & wallet
  *(Python • Tool/CLI • Ecash • bearer tokens, ecash)* —
  [Cashu](https://github.com/cashubtc/nutshell)
* **HWI** (Hardware Wallet Interface) – Standard CLI/lib for PSBT w/ hardware
  wallets *(Python • Tool/CLI • Bitcoin • PSBT, descriptors)* —
  [HWI](https://github.com/bitcoin-core/HWI)
* **JoinMarket** – CoinJoin coordinator + market maker
  *(Python • Tool/CLI • Bitcoin • coinjoin, liquidity)* —
  [JoinMarket](https://github.com/JoinMarket-Org/joinmarket-clientserver)
* **minisign** – Dead-simple file signing & verification (Ed25519)
  *(C • Tool/CLI • Crypto • release signing)* —
  [minisign](https://github.com/jedisct1/minisign)
* **Syncthing** – Encrypted P2P file sync
  *(Go • Tool/CLI • Networking/Privacy • file sync, LAN/mesh)* —
  [Syncthing](https://syncthing.net/)
* **Tailscale** – Managed WireGuard mesh with SSO & ACLs
  *(Go • Tool/CLI • Networking/Privacy • overlay VPN)* —
  [Tailscale](https://tailscale.com/kb/1017/what-is-tailscale)
* **WireGuard** – Minimal VPN toolkit
  *(C • Tool/CLI • Networking/Privacy • tunnels)* —
  [WireGuard](https://www.wireguard.com/)

---

## App Frameworks

* **Tauri** – Webview shell
  *(Rust/JS • Framework • App • desktop)* —
  [Tauri](https://tauri.app)
* **Wails** – Go webview shell
  *(Go/JS • Framework • App • desktop)* —
  [Wails](https://wails.io)

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
* **Topic**: Bitcoin, Lightning, Ecash, Nostr, Crypto, Auth, Networking/Privacy,
  Storage/Sync,
  Messaging/Comms, App
* **Language**: JS/TS, Rust, Go, C/C++, Java, Python, Multi, Spec
* **Use cases**: wallets, descriptors/miniscript, tx/PSBT, relays, node,
  routing, encryption, passkeys,
  sessions, file sync, anonymity overlays, desktop

---

## Roadmap for next expansion

* Expand **Networking/Privacy** coverage (e.g., mixnets, bridges) and add more
  **Tools/CLIs**
* Add **Storage/Sync** options (local-first/CRDTs) where relevant to sovereignty
* Add quick **comparison tables** (features, licenses, maintenance) as the
  catalog grows
