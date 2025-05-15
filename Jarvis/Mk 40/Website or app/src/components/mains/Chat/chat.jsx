import React, { useState } from "react";
import Btn from "../../Button/btn";

function Chat() {
  return (
    <>
    <div className="chatappmain">
        <div className="response">

        </div>
        <div className="request">
            <input type="text" className="requestsenderinp" />
        </div>
    </div>
    </>
  );
}

export default Chat;
