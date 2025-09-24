# freedom-tech
Suggested list of secure, adversarial, and otherwise freedom focused technologies, packages, and libraries to utilize for building sovereign apps.

This is all just tech that I know and use! There are many other amazing options that I am ignorant to!

## How this catalog is organized

* **By Type** → Libraries/SDKs, Runtimes/Servers, Tools/CLIs, Protocols/Standards
* **By Topic** → Bitcoin, Lightning, Nostr, Cryptography, Networking/Privacy, Auth/Sessions
* **By Language** → JavaScript/TypeScript, Rust, Go, Python, Multi‑lang
* **By Use Case** → Key mgmt, wallets, relays, signing, descriptors/miniscript, transport privacy, sessions, WebAuthn/Passkeys, etc.

> **Entry format**: `Name` – short note *(Language • Type • Topic • Use cases)* — \[link]

---

## Quick Index

* [By Type](#by-type)
* [By Topic](#by-topic)
* [By Language](#by-language)
* [Original List (normalized)](#original-list-normalized)
* [Tag Glossary](#tag-glossary)

---

## By Type

### Libraries / SDKs

* **bitcoinjs-lib** – Bitcoin primitives & tx building *(JS/TS • Library • Bitcoin • tx building, PSBT)* — [https://github.com/bitcoinjs/bitcoinjs-lib](https://github.com/bitcoinjs/bitcoinjs-lib)
* **bitcoinerlab/descriptors** – Output descriptors parsing/building *(JS/TS • Library • Bitcoin • descriptors)* — [https://github.com/bitcoinerlab/descriptors](https://github.com/bitcoinerlab/descriptors)
* **BDK** (Bitcoin Dev Kit) – Wallet & chain access toolkit *(Rust • Library • Bitcoin • wallets, descriptors)* — [https://bitcoindevkit.org/](https://bitcoindevkit.org/)
* **rust-bitcoin** – Core Bitcoin types *(Rust • Library • Bitcoin • primitives)* — [https://github.com/rust-bitcoin/rust-bitcoin](https://github.com/rust-bitcoin/rust-bitcoin)
* **rust-miniscript** – Miniscript & descriptors *(Rust • Library • Bitcoin • miniscript, policy)* — [https://github.com/rust-bitcoin/rust-miniscript](https://github.com/rust-bitcoin/rust-miniscript)
* **LDK** – Lightning Dev Kit *(Rust • Library • Lightning • node/wallet, routing)* — [https://lightningdevkit.org/](https://lightningdevkit.org/)
* **tonic\_lnd** – gRPC client for LND *(Rust • Library • Lightning • API client)* — [https://github.com/Kixunil/tonic\_lnd](https://github.com/Kixunil/tonic_lnd)
* **rust-nostr** – Nostr types & client *(Rust • Library • Nostr • client, events)* — [https://github.com/rust-nostr/nostr](https://github.com/rust-nostr/nostr)
* **nostr-tools** – Client utils *(JS/TS • Library • Nostr • keys, events, relay)* — [https://github.com/nbd-wtf/nostr-tools](https://github.com/nbd-wtf/nostr-tools)
* **go-nostr** – Nostr Go toolkit *(Go • Library • Nostr • client)* — [https://github.com/nbd-wtf/go-nostr](https://github.com/nbd-wtf/go-nostr)
* **NDK** – Nostr Dev Kit *(JS/TS • Library • Nostr • client, abstractions)* — [https://github.com/nostr-dev-kit/ndk](https://github.com/nostr-dev-kit/ndk)
* **SNSTR** – Minimal Nostr toolkit *(JS/TS • Library • Nostr • client, ergonomics)* — [https://github.com/austinkelsay/snstr](https://github.com/austinkelsay/snstr)
* **libsecp256k1** – secp256k1 curve impl *(C • Library • Crypto • ECDSA, Schnorr)* — [https://github.com/bitcoin-core/secp256k1](https://github.com/bitcoin-core/secp256k1)
* **@noble/curves** – Pure JS curves *(JS/TS • Library • Crypto • secp256k1/ed25519)* — [https://github.com/paulmillr/noble-curves](https://github.com/paulmillr/noble-curves)
* **@noble/hashes** – Hash suites *(JS/TS • Library • Crypto • SHA‑256, Blake3, etc.)* — [https://github.com/paulmillr/noble-hashes](https://github.com/paulmillr/noble-hashes)
* **@noble/ciphers** – Stream & AEAD *(JS/TS • Library • Crypto • ChaCha20‑Poly1305, etc.)* — [https://github.com/paulmillr/noble-ciphers](https://github.com/paulmillr/noble-ciphers)
* **@noble/post-quantum** – PQ experiments *(JS/TS • Library • Crypto)* — [https://github.com/paulmillr/noble-post-quantum](https://github.com/paulmillr/noble-post-quantum)
* **scure-bip39** – Mnemonics *(JS/TS • Library • Crypto/Bitcoin • seed gen)* — [https://github.com/paulmillr/scure-bip39](https://github.com/paulmillr/scure-bip39)
* **scure-bip32** – HD derivation *(JS/TS • Library • Crypto/Bitcoin • key derivation)* — [https://github.com/paulmillr/scure-bip32](https://github.com/paulmillr/scure-bip32)
* **scure-btc-signer** – Lightweight PSBT/signing *(JS/TS • Library • Bitcoin • signer)* — [https://github.com/paulmillr/scure-btc-signer](https://github.com/paulmillr/scure-btc-signer)
* **scure-base** – bech32/base58/base64 *(JS/TS • Library • Crypto • encodings)* — [https://github.com/paulmillr/scure-base](https://github.com/paulmillr/scure-base)
* **simplewebauthn** – WebAuthn/Passkeys server & browser *(JS/TS • Library • Auth • passkeys)* — [https://github.com/MasterKale/SimpleWebAuthn](https://github.com/MasterKale/SimpleWebAuthn)

### Runtimes / Servers

* **relayer** – Nostr relay framework *(Go • Server • Nostr)* — [https://github.com/fiatjaf/relayer](https://github.com/fiatjaf/relayer)
* **nostr-rs-relay** – High‑perf relay *(Rust • Server • Nostr)* — [https://github.com/scsibug/nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay)
* **Core Lightning (CLN)** – Lightning node *(C • Server • Lightning)* — [https://github.com/ElementsProject/lightning](https://github.com/ElementsProject/lightning)
* **btcd** – Full node implementation *(Go • Server • Bitcoin)* — [https://github.com/btcsuite/btcd](https://github.com/btcsuite/btcd)

### Protocols / Standards

* **NIP‑44** – Nostr encrypted DMs *(Spec • Nostr • encryption)* — [https://github.com/paulmillr/nip44](https://github.com/paulmillr/nip44)

### Tools / CLIs

*(Add as we grow: minisign, age, HWI, lncli, lightning‑cli, etc.)*

---

## By Topic

### Bitcoin

* **rust-bitcoin** — primitives *(Rust • Lib)*
* **BDK** — wallet toolkit *(Rust • Lib)*
* **bitcoinjs-lib** — tx & PSBT *(JS/TS • Lib)*
* **bitcoinerlab/descriptors** — descriptors *(JS/TS • Lib)*
* **rust-miniscript** — miniscript *(Rust • Lib)*
* **btcd** — full node *(Go • Server)*
* **scure‑bip39 / bip32 / btc‑signer / base** *(JS/TS • Lib)*

### Lightning

* **LDK** — node/wallet *(Rust • Lib)*
* **tonic\_lnd** — gRPC client *(Rust • Lib)*
* **Core Lightning (CLN)** — node *(C • Server)*

### Nostr

* **rust-nostr** *(Rust • Lib)*
* **nostr-tools** *(JS/TS • Lib)*
* **go-nostr** *(Go • Lib)*
* **NDK** *(JS/TS • Lib)*
* **SNSTR** *(JS/TS • Lib)*
* **relayer** *(Go • Server)*
* **nostr-rs-relay** *(Rust • Server)*
* **NIP‑44** *(Spec)*

### Cryptography

* **libsecp256k1** *(C • Lib)*
* **@noble/{curves,hashes,ciphers,post‑quantum}** *(JS/TS • Lib)*
* **scure‑{bip39,bip32,btc‑signer,base}** *(JS/TS • Lib)*

### Auth / Sessions

* **iron-session** — stateless encrypted cookies *(JS/TS • Lib)*
* **simplewebauthn** — WebAuthn/Passkeys *(JS/TS • Lib)*

*(Networking/Privacy category placeholder → Tor, WireGuard, I2P, etc. to be added later.)*

---

## By Language

### JavaScript / TypeScript

* **bitcoinjs-lib**, **bitcoinerlab/descriptors** *(Bitcoin)*
* **nostr-tools**, **NDK**, **SNSTR** *(Nostr)*
* **@noble/{curves,hashes,ciphers,post‑quantum}**, **scure‑{bip39,bip32,btc‑signer,base}** *(Crypto)*
* **simplewebauthn**, **iron-session** \*(Auth)

### Rust

* **BDK**, **rust-bitcoin**, **rust-miniscript** *(Bitcoin)*
* **LDK**, **tonic\_lnd** *(Lightning)*
* **rust-nostr** *(Nostr)*
* **nostr-rs-relay** \*(Server)

### Go

* **btcd** *(Bitcoin server)*
* **go-nostr** *(Nostr lib)*
* **relayer** *(Nostr server framework)*

### C / C++

* **libsecp256k1** *(Crypto)*
* **Core Lightning (CLN)** *(Lightning server)*

---

## Original List (normalized)

### Bitcoin

* bitcoinjs-lib — [https://github.com/bitcoinjs/bitcoinjs-lib](https://github.com/bitcoinjs/bitcoinjs-lib)
* bitcoinerlab/descriptors — [https://github.com/bitcoinerlab/descriptors](https://github.com/bitcoinerlab/descriptors)
* BDK — [https://bitcoindevkit.org/](https://bitcoindevkit.org/)
* rust-bitcoin — [https://github.com/rust-bitcoin/rust-bitcoin](https://github.com/rust-bitcoin/rust-bitcoin)

### Lightning

* LDK — [https://lightningdevkit.org/](https://lightningdevkit.org/)
* tonic\_lnd — [https://github.com/Kixunil/tonic\_lnd](https://github.com/Kixunil/tonic_lnd)

### Nostr

* rust-nostr — [https://github.com/rust-nostr/nostr](https://github.com/rust-nostr/nostr)
* nostr-tools — [https://github.com/nbd-wtf/nostr-tools](https://github.com/nbd-wtf/nostr-tools)
* go-nostr — [https://github.com/nbd-wtf/go-nostr](https://github.com/nbd-wtf/go-nostr)
* NDK — [https://github.com/nostr-dev-kit/ndk](https://github.com/nostr-dev-kit/ndk)
* SNSTR — [https://github.com/austinkelsay/snstr](https://github.com/austinkelsay/snstr)
* Relays: relayer — [https://github.com/fiatjaf/relayer](https://github.com/fiatjaf/relayer)
* NIP44: paulmillr/nip44 — [https://github.com/paulmillr/nip44](https://github.com/paulmillr/nip44)

### Cryptography

* secp256k1: libsecp256k1 — [https://github.com/bitcoin-core/secp256k1](https://github.com/bitcoin-core/secp256k1)
* Noble: @noble/{ciphers,hashes,curves,post-quantum} — [https://github.com/paulmillr](https://github.com/paulmillr)
* Scure: scure‑{base,bip32,btc‑signer,bip39} — [https://github.com/paulmillr](https://github.com/paulmillr)

### Authentication

* Sessions: iron-session — [https://www.npmjs.com/package/iron-session](https://www.npmjs.com/package/iron-session)

---

## Tag Glossary

* **Type**: Library, Server (Runtime), Tool/CLI, Spec
* **Topic**: Bitcoin, Lightning, Nostr, Crypto, Auth, Networking/Privacy
* **Language**: JS/TS, Rust, Go, C/C++, Multi
* **Use cases**: wallets, descriptors/miniscript, tx/PSBT, relays, node, routing, encryption, passkeys, sessions

---

## Roadmap for next expansion

* Add **Networking/Privacy** (Tor, WireGuard, I2P) and **Tools/CLIs** (age, minisign, HWI, lncli, lightning‑cli)
* Add **Storage/Sync** options (e.g., local‑first, CRDTs) where relevant to sovereignty
* Add quick **comparison tables** (features, licenses, maintenance) as the catalog grows
