# freedom-tech
Suggested list of secure, adversarial, and otherwise freedom focused technologies, packages, and libraries to utilize for building sovereign apps.

This is all just tech that I know and use! There are many other amazing options that I am ignorant to!

## Libraries / Packages:

### Bitcoin:
- [bitcoinjs-lib](https://github.com/bitcoinjs/bitcoinjs-lib)
- [bitcoinerlab/descriptors](https://github.com/bitcoinerlab/descriptors)
- [BDK](https://bitcoindevkit.org/)
- [rust-bitcoin](https://github.com/rust-bitcoin/rust-bitcoin)

### Lightning:
- [LDK](https://lightningdevkit.org/)
- [tonic_lnd](https://github.com/Kixunil/tonic_lnd)

### Nostr

#### Nostr Development Kits:
- [rust-nostr](https://github.com/rust-nostr/nostr)
- [nostr-tools](https://github.com/nbd-wtf/nostr-tools)
- [go-nostr](https://github.com/nbd-wtf/go-nostr)
- [NDK](https://github.com/nostr-dev-kit/ndk)
- [SNSTR](https://github.com/austinkelsay/snstr)

#### Nostr Relays:
- [relayer](https://github.com/fiatjaf/relayer)

#### NIP44:
- [nip44 (paulmillr)](https://github.com/paulmillr/nip44)

### Cryptography:

#### ECC / Hashes:

##### secp256k1
- [libsecp256k1](https://github.com/bitcoin-core/secp256k1)

##### Noble (paulmillr)
- [@noble/ciphers](https://github.com/paulmillr/noble-ciphers)
- [@noble/hashes](https://github.com/paulmillr/noble-hashes)
- [@noble/curves](https://github.com/paulmillr/noble-curves)
  - Lightweight variants: [@noble/secp256k1](https://github.com/paulmillr/noble-secp256k1) & [@noble/ed25519](https://github.com/paulmillr/noble-ed25519)  
- [@noble/post-quantum](https://github.com/paulmillr/noble-post-quantum)

##### Scure micro-libraries
- [scure-base, base64, bech32](https://github.com/paulmillr/scure-base)
- [scure-bip32](https://github.com/paulmillr/scure-bip32)
- [scure-btc-signer](https://github.com/paulmillr/scure-btc-signer)
- [scure-bip39](https://github.com/paulmillr/scure-bip39)

### Auth / Sessions
- [iron-session](https://www.npmjs.com/package/iron-session)
