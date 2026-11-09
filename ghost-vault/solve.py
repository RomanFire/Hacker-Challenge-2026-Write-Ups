import ghost_vault as gv

def run(keys):
    chain, lane = b"", None
    for n, key in enumerate(keys):
        payload, lane = gv._unlock(n, key, chain, lane)
        if not payload:
            return f"failed at stage {n + 1} ({key})"
        print(f"  stage {n + 1} [{key}] lane={lane}: {payload['msg']}")
        chain = bytes.fromhex(payload["chain"])
    return "done"

print("Intended path:")
print(run(["GHOST", "WIRE", "MIDNIGHT GHOSTS NEVER SLEEP"]))
print("Decoy path:")
print(run(["HAUNT", "COPPER", "SERVER ROOM"]))
print("Mixed (should fail):")
print(run(["HAUNT", "WIRE"]))
