import React from "react";
import { Switch } from "react-router-dom";
import Route from "./Route";

import Login from "../components/login";

export default function Routes() {
  return (
    <Switch>
      <Route path="/login" exact component={Login} />

      {/* redirect user to Login page if route does not exist and user is not authenticated */}
      <Route component={Login} />
    </Switch>
  );
}
