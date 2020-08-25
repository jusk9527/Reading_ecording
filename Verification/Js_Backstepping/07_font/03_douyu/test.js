const encode = obj => Object.keys(obj).map(k => `${ k }@=${ obj[k] }`).join("/")

const decode = str => {
  return str.split("/").reduce((acc, pair) => {
    const [key, value] = pair.split("@=")
    acc[key] = value
    return acc
  }, {})
}

const crypto = require("crypto")
const md5Hash = crypto.createHash("md5")
const md5 = payload => {
  return md5Hash.update(payload).digest("hex")
}
// 4-byte length, 4-byte length, 0xb102, 0x0000
const getPayload = obj => {
  const arr = [0, 0, 0, 0, 0, 0, 0, 0, 0xb1, 0x02, 0x00, 0x00]

  const objEncoded = encode(obj) + "/\x00"
  arr.push(...objEncoded.split("").map(c => c.charCodeAt(0)))

  const payload = Buffer.from(arr)
  const dv = new DataView(payload.buffer, payload.byteOffset)
  const length = payload.length - 4
  dv.setUint32(0, length, true)
  dv.setUint32(4, length, true)

  return payload
}

ws.on("open", () => {
  // 这个随便填写一个
  const devID = "4d9c39a8a93746b6db53675800021501"

  const rt = (new Date().getTime() / 1000) >> 0

  const obj = {
    type: "loginreq",
    roomid: roomID,
    devid: devID,
    rt: rt,
    vk: md5(rt + "r5*^5;}2#${XF[h+;'./.Q'1;,-]f'p[" + devID),
  }

  const payload = getPayload(obj)
  ws.send(payload)
})

ws.on("message", payload => {
  const data = decode(payload.slice(12).toString())
  if(data.type === "followed_count") {
    console.log(data)
  } else {
    console.log(data.type)
  }
})